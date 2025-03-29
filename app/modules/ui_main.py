from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget,
    QGridLayout,
    QSizePolicy,
    QLineEdit,
)
from PySide6.QtGui import QPixmap, QPainter, QIntValidator, QIcon
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt, QSize
from app.libs.main import onClickVideos
from app.i18n import _
from app.assets.resource_manager import ResourceManager
from app.assets import resources_rc
from app.utils.logger.logger import logger


# template
class ItemWidget(QWidget):
    clicked = Signal()
    
    def __init__(self, cover_image_path: str, title: str, *args, **kwargs):
        super(ItemWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout()

        # cover
        self.cover_label = QLabel(self)
        pixmap = QPixmap(cover_image_path)
        self.cover_label.setPixmap(pixmap)
        self.cover_label.setScaledContents(True)  # zoom cover image
        layout.addWidget(self.cover_label)

        # allowd to zoom cover image
        self.cover_label.setSizePolicy(
            QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        )

        # title
        self.title_label = QLabel(title, self)
        self.title_label.setStyleSheet("color: white;font-size: 16px;")
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        self.setLayout(layout)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()  # Emit clicked signal
        super().mousePressEvent(event)


class PageWidget(QWidget):
    def __init__(self, items_data=list, *args, **kwargs):
        super(PageWidget, self).__init__(*args, **kwargs)
        layout = QGridLayout()
        # set grid layout
        for i, item_data in enumerate(items_data):
            item = ItemWidget(item_data["cover"], item_data["title"])
            item.clicked.connect(lambda v=item_data["vid"]: onClickVideos(v))
            layout.addWidget(item, i // 3, i % 3)  # 3x3

            # set item size
            item.setSizePolicy(
                QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            )

        layout.setSpacing(10)  # set spacing between items
        layout.setContentsMargins(20, 10, 20, 20)
        self.setLayout(layout)


class Ui_MainWindow(object):
    def setupUi(self, MainWin, pages_data=[]):
        # super(Ui_MainWindow, self).__init__()
        if not MainWin.objectName():
            MainWin.setObjectName("Form")
        self.setWindowTitle(_("Videos"))

        self.res_mgr = ResourceManager()
        self.toolbar_btns = [
            {
                "name": "user_profile_btn",
                "icon": ":/icons/icons/user_x48.svg",
            },
            {
                "name": "setting_btn",
                "icon": ":/icons/icons/setting.svg",
            },
        ]
        self.bg_image_path = ":/images/images/background.png"  # using QRC path
        self.def_cover_path = ":/covers/covers/default.png"  # using QRC path
        self.button_qss = self.res_mgr.load(":/qss/qss/button.qss")
        self.line_edit_qss = self.res_mgr.load(":/qss/qss/line_edit.qss")
        self.setStyleSheet(
            "QWidget#Form {\n" f"	background-image: url({self.bg_image_path})\n" "}"
        )
        # Prog layout
        #         ↓ start from 0
        # Pages: |0|1|2|...|n|
        # User layout
        #           ↓ start from 1
        # Pages: |0|1|2|3|...|n+1|
        self.current_page = 0
        self.main_layout = QVBoxLayout(self)
        self.bar_layout = QHBoxLayout()
        self.button_layout = QHBoxLayout()
        self.toolbar = QHBoxLayout()
        self.stacked_widget = QStackedWidget(self)
        
        # Add toolbar layout at the left top
        self.toolbar.setAlignment(Qt.AlignLeft)
        self.toolbar.setContentsMargins(20, 10, 20, 0)
        
        self.createToolbarButtons()
        self.createSearchBox()
        self.main_layout.addLayout(self.toolbar)

        # next pages btn layout
        self.pages_data: list[dict] = pages_data
        self.page_cache = {}  # cache videos page

        # load frist page
        self.loadPage(0)
        self.main_layout.addWidget(self.stacked_widget)

        # next page btn
        self.prev_button = QPushButton(_("上一页"), self)
        self.prev_button.setStyleSheet(self.button_qss)

        self.next_button = QPushButton(_("下一页"), self)
        self.next_button.setStyleSheet(self.button_qss)

        self.label = QLabel(_("第"), self)
        self.label.setStyleSheet("color: white;font-size: 16px;")
        self.label.setFixedWidth(20)

        self.label2 = QLabel(_("页"), self)
        self.label2.setStyleSheet("color: white;font-size: 16px;")
        self.label2.setFixedWidth(20)

        self.page_number = QLineEdit(self)
        # set page number
        self.page_number.setFixedSize(50, 50)
        self.page_number.setStyleSheet("color: black;font-size: 16px;")
        self.page_number.setValidator(
            QIntValidator(1, len(self.pages_data), self))
        self.page_number.setText(str(self.current_page + 1))

        # add buttons to layout
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.next_button)
        self.button_layout.addWidget(self.label)
        self.button_layout.addWidget(self.label2)
        self.button_layout.addWidget(self.page_number)
        self.main_layout.addLayout(self.button_layout)

    def createSearchBox(self):
        self.search_box = QLineEdit(self)
        self.search_box.setObjectName("search_box")
        self.search_box.setPlaceholderText(_("搜索"))
        self.search_box.setFixedSize(500, 48)
        self.search_box.setStyleSheet(self.line_edit_qss)
        self.toolbar.addWidget(self.search_box)

    def createToolbarButtons(self):
        for button in self.toolbar_btns:
            btn = QPushButton("", self)
            btn.setIcon(QIcon(button["icon"]))
            btn.setFixedSize(48, 48)
            btn.setStyleSheet("QPushButton { border: none; }")
            btn.setIconSize(QSize(48, 48))
            setattr(self, button["name"], btn)
            self.toolbar.addWidget(btn)
            self.toolbar.addSpacing(10)  # Add spacing between buttons
