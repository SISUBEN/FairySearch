import pdb
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
# import PySide6.QtGui as QtGui
from PySide6.QtCore import Qt, QSize
from app.libs.main import onClickVideos
from .assets import resources_rc
from app.modules.logger.logger import logger

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
        self.title_label.setStyleSheet("color: white;weight: bold;font-size: 16px;")
        self.title_label.setAlignment(Qt.AlignCenter)  # 标题居中
        layout.addWidget(self.title_label)

        self.setLayout(layout)
        
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()  # Emit the custom clicked signal
        super().mousePressEvent(event)


class PageWidget(QWidget):
    def __init__(self, items_data = list, *args, **kwargs):
        super(PageWidget, self).__init__(*args, **kwargs)
        layout = QGridLayout()
        # set grid layout
        for i, item_data in enumerate(items_data):
            item = ItemWidget(item_data["cover"], item_data["title"])
            logger.debug(f"item_data: {item_data}")
            # pdb.set_trace()
            logger.debug(f"clicked video id: {item_data['vid']}")
            item.clicked.connect(lambda v=item_data["vid"]: onClickVideos(v))
            layout.addWidget(item, i // 3, i % 3)  # 3x3

            # set item size
            item.setSizePolicy(
                QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            )

        layout.setSpacing(10)  # set spacing between items
        layout.setContentsMargins(20, 45, 20, 20)
        self.setLayout(layout)

class Ui_MainWindow(object):
    def setupUi(self, MainWin, pages_data = []):
        # super(Ui_MainWindow, self).__init__()
        if not MainWin.objectName():
            MainWin.setObjectName("Form")
        self.setWindowTitle("Videos")
        # self.bg_image_path = "./assets/images/background.png" # using absolute path
        self.bg_image_path = ":/images/images/background.png"  # using QRC path
        # self.def_cover_path = "./assets/covers/default.png" # using absolute path
        self.def_cover_path = ":/covers/covers/default.png"  # using QRC path
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
        # next pages btn layout
        self.stacked_widget = QStackedWidget(self)
        self.pages_data: list[dict] = pages_data
        self.page_cache = {}  # cache videos page
        # load frist page
        self.loadPage(0)
        self.main_layout.addWidget(self.stacked_widget)
        # user profile btn
        self.user_profile_btn = QPushButton("", self)
        # next page btn
        self.button_layout = QHBoxLayout()
        self.prev_button = QPushButton("上一页", self)
        self.next_button = QPushButton("下一页", self)
        self.label = QLabel("第", self)
        self.page_number = QLineEdit(self)
        self.label2 = QLabel("页", self)
        self.prev_button.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(0, 0, 0);\n"
            "    color: white;\n"
            "    border: 3px solid #262626;\n"
            "    height: 50px;\n"
            "    width: 500px;\n"
            "    border-radius: 25px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: #a6c100;\n"
            "    color: black;\n"
            "    border: 5px solid #a6c100;\n"
            "}"
        )
        self.next_button.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(0, 0, 0);\n"
            "    color: white;\n"
            "    border: 3px solid #262626;\n"
            "    height: 50px;\n"
            "    width: 500px;\n"
            "    border-radius: 25px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: #a6c100;\n"
            "    color: black;\n"
            "    border: 5px solid #a6c100;\n"
            "}"
        )
        self.label.setStyleSheet("color: white;weight: bold;font-size: 16px;")
        self.label.setFixedWidth(20)
        self.label2.setFixedWidth(20)
        self.label2.setStyleSheet("color: white;weight: bold;font-size: 16px;")
        self.page_number.setFixedSize(50, 50)
        self.page_number.setStyleSheet("color: black;weight: bold;font-size: 16px;")
        self.page_number.setValidator(QIntValidator(1, len(self.pages_data), self))
        self.page_number.setText(str(self.current_page + 1))
        self.user_profile_btn.setIcon(QIcon(":/icons/icons/user_x48.svg"))
        self.user_profile_btn.setFixedSize(48, 48)
        # set button position
        self.user_profile_btn.move(self.user_profile_btn.width() - 10, 8)
        self.user_profile_btn.setStyleSheet("QPushButton { border: none; }")
        self.user_profile_btn.setIconSize(QSize(48, 48))
        # add buttons to layout
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.label)
        self.button_layout.addWidget(self.page_number)
        self.button_layout.addWidget(self.label2)
        self.button_layout.addWidget(self.next_button)
        self.main_layout.addLayout(self.button_layout)

    