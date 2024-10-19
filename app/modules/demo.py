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

# import PySide6.QtGui as QtGui
from PySide6.QtCore import Qt, QSize
import sys
from assets import resources_rc


# 模板类
class ItemWidget(QWidget):
    def __init__(self, cover_image_path: str, title: str, *args, **kwargs):
        super(ItemWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout()

        # 封面图片
        self.cover_label = QLabel(self)
        pixmap = QPixmap(cover_image_path)
        self.cover_label.setPixmap(pixmap)
        self.cover_label.setScaledContents(True)  # 自动缩放封面图片
        layout.addWidget(self.cover_label)

        # 允许封面图片在窗口中水平和垂直方向上自适应拉伸
        self.cover_label.setSizePolicy(
            QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        )

        # 标题
        self.title_label = QLabel(title, self)
        self.title_label.setStyleSheet("color: white;weight: bold;font-size: 16px;")
        self.title_label.setAlignment(Qt.AlignCenter)  # 标题居中
        layout.addWidget(self.title_label)

        self.setLayout(layout)


class PageWidget(QWidget):
    def __init__(self, items_data, *args, **kwargs):
        super(PageWidget, self).__init__(*args, **kwargs)
        layout = QGridLayout()
        # 将每个项目以3列的方式排列
        for i, item_data in enumerate(items_data):
            item = ItemWidget(item_data["cover"], item_data["title"])
            layout.addWidget(item, i // 3, i % 3)  # 3列布局

            # 设置项目部件的大小策略，使其可以自动拉伸
            item.setSizePolicy(
                QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            )

        layout.setSpacing(10)  # 设置每个项目之间的间距
        layout.setContentsMargins(20, 45, 20, 20)
        self.setLayout(layout)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Videos")
        self.setObjectName("Form")

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

        # 主布局
        self.main_layout = QVBoxLayout(self)
        # 栏目布局
        self.bar_layout = QHBoxLayout()
        # 翻页内容部分
        self.stacked_widget = QStackedWidget(self)

        self.pages_data: list[dict] = [
            [
                {"cover": self.def_cover_path, "title": "Item 1"},
                {"cover": self.def_cover_path, "title": "Item 2"},
                {"cover": self.def_cover_path, "title": "Item 3"},
                {"cover": self.def_cover_path, "title": "Item 4"},
                {"cover": self.def_cover_path, "title": "Item 5"},
                {"cover": self.def_cover_path, "title": "Item 6"},
            ],
            [
                {"cover": self.def_cover_path, "title": "Item 7"},
                {"cover": self.def_cover_path, "title": "Item 8"},
                {"cover": self.def_cover_path, "title": "Item 9"},
                {"cover": self.def_cover_path, "title": "Item 10"},
                {"cover": self.def_cover_path, "title": "Item 11"},
                {"cover": self.def_cover_path, "title": "Item 12"},
            ],
            [
                {"cover": self.def_cover_path, "title": "Item 13"},
                {"cover": self.def_cover_path, "title": "Item 14"},
                {"cover": self.def_cover_path, "title": "Item 15"},
                {"cover": self.def_cover_path, "title": "Item 16"},
                {"cover": self.def_cover_path, "title": "Item 17"},
                {"cover": self.def_cover_path, "title": "Item 18"},
            ],
        ]

        self.page_cache = {}  # 用于缓存已经加载过的页面

        # 加载第一页
        self.load_page(0)
        self.main_layout.addWidget(self.stacked_widget)

        # user profile btn
        self.user_profile_btn = QPushButton("", self)

        # 翻页按钮布局
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
        # 设置位置在窗口的右上角
        self.user_profile_btn.move(self.user_profile_btn.width() - 10, 8)
        self.user_profile_btn.setStyleSheet("QPushButton { border: none; }")
        self.user_profile_btn.setIconSize(QSize(48, 48))

        # bind button click events
        self.prev_button.clicked.connect(self.show_prev_page)
        self.next_button.clicked.connect(self.show_next_page)
        self.page_number.editingFinished.connect(self.jump_to_page)
        self.user_profile_btn.clicked.connect(self.show_user_profile)

        # add buttons to layout
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.label)
        self.button_layout.addWidget(self.page_number)
        self.button_layout.addWidget(self.label2)
        self.button_layout.addWidget(self.next_button)
        self.main_layout.addLayout(self.button_layout)

        self.update_buttons()

    # def resizeEvent(self, event):
    #     palette = QtGui.QPalette()
    #     pix = QtGui.QPixmap(f"{self.bg_image_path}")
    #     pix = pix.scaled(self.width(),self.height())
    #     palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pix))
    #     self.setPalette(palette)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(f"{self.bg_image_path}")
        # pixmap = QPixmap(":/images/background.png")
        painter.drawPixmap(self.rect(), pixmap)

    def jump_to_page(self) -> None:
        page_num = int(self.page_number.text())
        if page_num < 0 or page_num < len(self.pages_data) - 1:
            return
        self.current_page = page_num - 1
        self.load_page(self.current_page)
        self.update_buttons()
        
    def show_user_profile(self):
        pass
        
    # Lazy loading
    def load_page(self, page_index: int) -> None:
        if page_index not in self.page_cache:
            if 0 <= page_index < len(self.pages_data):
                page = PageWidget(self.pages_data[page_index])
                self.stacked_widget.addWidget(page)
                self.page_cache[page_index] = page  # 缓存加载过的页面
        self.stacked_widget.setCurrentIndex(page_index)

    def show_prev_page(self) -> None:
        if self.current_page > 0:
            self.current_page -= 1
            self.page_number.setText(str(self.current_page + 1))
            self.load_page(self.current_page)  # 加载当前页
            self.update_buttons()

    def show_next_page(self) -> None:
        if self.current_page < len(self.pages_data) - 1:
            self.current_page += 1
            self.page_number.setText(str(self.current_page + 1))
            self.load_page(self.current_page)  # 加载下一页
            self.update_buttons()

    def update_buttons(self) -> None:
        self.prev_button.setEnabled(self.current_page > 0)
        self.next_button.setEnabled(self.current_page < len(self.pages_data) - 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
