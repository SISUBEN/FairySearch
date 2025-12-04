from typing import Callable
from app import (
    QWidget,
    QApplication,
    logger,
    QPainter,
    QPixmap,
    QPushButton,
    QGridLayout,
    QStackedWidget,
    QLabel,
    QLineEdit
)
from PySide6.QtWidgets import QVBoxLayout, QSizePolicy
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QMouseEvent
from app.database.search import Searchdb
from app.utils.time import TimeKeeper
from app.i18n import _
from app.libs.video_browser import VideoBrowser
from app.libs.exception import VideoNotFoundError


def onClickVideos(vid: int) -> None:
    try:
        video_browser = VideoBrowser(vid)
        video_browser.show()
    except VideoNotFoundError as e:
        logger.error(f"Video not found: {e}")


class ItemWidget(QWidget):
    clicked = Signal()
    
    def __init__(self, vid: int, title: str, cover_path: str, tags: str, desc: str, click_callback: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vid = vid
        self.click_callback = click_callback
        
        layout = QVBoxLayout()

        # cover
        self.cover_label = QLabel(self)
        # Handle Default enum value
        if hasattr(cover_path, 'value'):
            cover_path = cover_path.value
        pixmap = QPixmap(cover_path)
        self.cover_label.setPixmap(pixmap)
        self.cover_label.setScaledContents(True)
        layout.addWidget(self.cover_label)

        # allow to zoom cover image
        self.cover_label.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        )

        # title
        self.title_label = QLabel(title, self)
        self.title_label.setStyleSheet("color: white;font-size: 16px;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label)

        self.setLayout(layout)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.click_callback(self.vid)
        super().mousePressEvent(event)


class PageWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(PageWidget, self).__init__(*args, **kwargs)
        self.layout_grid = QGridLayout()
        self.layout_grid.setSpacing(10)
        self.layout_grid.setContentsMargins(20, 10, 20, 20)
        self.setLayout(self.layout_grid)


class SearchWindow(QWidget):
    def __init__(self, search_results: list, keyword: str, app: QApplication) -> None:
        super().__init__()
        self.app = app
        self.search_results = search_results
        self.keyword = keyword
        self.current_page = 0
        self.search_cache = {}
        
        # Set window attributes to keep it alive
        self.setAttribute(Qt.WA_DeleteOnClose, False)
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        
        # Setup UI
        self.setupUi()
        
        # Load first page
        self.loadSearchPage(0)
        
        # Disable zoom
        self.setFixedSize(800, 600)
        
    def setupUi(self):
        self.setWindowTitle(_(f"搜索结果 - {self.keyword}"))
        self.setGeometry(200, 200, 800, 600)
        
        # Create main layout
        main_layout = QGridLayout(self)
        
        # Create search results widget
        self.search_results_widget = QStackedWidget()
        main_layout.addWidget(self.search_results_widget, 0, 0, 1, 5)
        
        # Create navigation buttons
        self.prev_button = QPushButton(_("上一页"))
        self.prev_button.clicked.connect(self.showPrevPage)
        main_layout.addWidget(self.prev_button, 1, 0)
        
        self.next_button = QPushButton(_("下一页"))
        self.next_button.clicked.connect(self.showNextPage)
        main_layout.addWidget(self.next_button, 1, 1)
        
        # Page info label
        self.page_label = QLabel(_("页码:"))
        main_layout.addWidget(self.page_label, 1, 2)
        
        self.page_number = QLineEdit("1")
        self.page_number.setMaximumWidth(50)
        self.page_number.returnPressed.connect(self.jump2Page)
        main_layout.addWidget(self.page_number, 1, 3)
        
        # Close button
        self.close_button = QPushButton(_("关闭"))
        self.close_button.clicked.connect(self.close)
        main_layout.addWidget(self.close_button, 1, 4)
        
        # Update button states
        self.updateButtons()
        
    def loadSearchPage(self, page_index: int) -> None:
        # Check if page is already cached
        if page_index in self.search_cache:
            cached_widget = self.search_cache[page_index]
            self.search_results_widget.setCurrentWidget(cached_widget)
            self.current_page = page_index
            self.page_number.setText(str(page_index + 1))
            return
            
        # Create new page widget
        if page_index < len(self.search_results):
            result_data = self.search_results[page_index]
            page_widget = PageWidget()
            
            # Create item widget for this result
            item_widget = ItemWidget(
                result_data["vid"],
                result_data["title"],
                result_data["cover"],
                "",  # tags not available in converted format
                "",  # desc not available in converted format
                onClickVideos
            )
            
            # Add item to page
            page_widget.layout_grid.addWidget(item_widget, 0, 0)
            
            # Cache and add to widget
            self.search_cache[page_index] = page_widget
            self.search_results_widget.addWidget(page_widget)
            self.search_results_widget.setCurrentWidget(page_widget)
            
            # Update current page
            self.current_page = page_index
            self.page_number.setText(str(page_index + 1))
            
    def showPrevPage(self) -> None:
        if self.current_page > 0:
            self.current_page -= 1
            self.loadSearchPage(self.current_page)
            self.updateButtons()
            
    def showNextPage(self) -> None:
        if self.current_page < len(self.search_results) - 1:
            self.current_page += 1
            self.loadSearchPage(self.current_page)
            self.updateButtons()
            
    def jump2Page(self) -> None:
        try:
            page_num = int(self.page_number.text())
            if page_num < 1 or page_num > len(self.search_results):
                return
            target_page = page_num - 1
            self.current_page = target_page
            self.loadSearchPage(target_page)
            self.updateButtons()
        except ValueError:
            # Invalid input, ignore
            pass
            
    def updateButtons(self) -> None:
        # Update previous button
        self.prev_button.setEnabled(self.current_page > 0)
        
        # Update next button
        self.next_button.setEnabled(self.current_page < len(self.search_results) - 1)
        
    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        pixmap = QPixmap(":/images/bg.jpg")
        painter.drawPixmap(self.rect(), pixmap)