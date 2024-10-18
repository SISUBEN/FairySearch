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
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys


class ItemWidget(QWidget):
    def __init__(self, cover_image_path, title, *args, **kwargs):
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
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Videos")

        # 主布局
        main_layout = QVBoxLayout(self)

        # 翻页内容部分
        self.stacked_widget = QStackedWidget(self)

        # 这里模拟了大量的数据，但我们只在需要时加载
        self.pages_data = [
            [
                {"cover": "./assets/covers/default.png", "title": "Item 1"},
                {"cover": "./assets/covers/default.png", "title": "Item 2"},
                {"cover": "./assets/covers/default.png", "title": "Item 3"},
                {"cover": "./assets/covers/default.png", "title": "Item 4"},
                {"cover": "./assets/covers/default.png", "title": "Item 5"},
                {"cover": "./assets/covers/default.png", "title": "Item 6"},
            ],
            [
                {"cover": "./assets/covers/default.png", "title": "Item 7"},
                {"cover": "./assets/covers/default.png", "title": "Item 8"},
                {"cover": "./assets/covers/default.png", "title": "Item 9"},
                {"cover": "./assets/covers/default.png", "title": "Item 10"},
                {"cover": "./assets/covers/default.png", "title": "Item 11"},
                {"cover": "./assets/covers/default.png", "title": "Item 12"},
            ],
            [
                {"cover": "./assets/covers/default.png", "title": "Item 13"},
                {"cover": "./assets/covers/default.png", "title": "Item 14"},
                {"cover": "./assets/covers/default.png", "title": "Item 15"},
                {"cover": "./assets/covers/default.png", "title": "Item 16"},
                {"cover": "./assets/covers/default.png", "title": "Item 17"},
                {"cover": "./assets/covers/default.png", "title": "Item 18"},
            ],
        ]

        self.page_cache = {}  # 用于缓存已经加载过的页面

        # 加载第一页
        self.load_page(0)
        main_layout.addWidget(self.stacked_widget)

        # 翻页按钮布局
        button_layout = QHBoxLayout()
        self.prev_button = QPushButton("上一页", self)
        self.next_button = QPushButton("下一页", self)
        self.prev_button.setStyleSheet(u"QPushButton {\n"
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
        "}")
        self.next_button.setStyleSheet(u"QPushButton {\n"
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
        "}")
         
        # bind button click events
        self.prev_button.clicked.connect(self.show_previous_page)
        self.next_button.clicked.connect(self.show_next_page)

        # add buttons to layout
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)
        main_layout.addLayout(button_layout)

        self.current_page = 0
        self.update_buttons()

    # Lazy loading 
    def load_page(self, page_index):
        if page_index not in self.page_cache:
            if 0 <= page_index < len(self.pages_data):
                page = PageWidget(self.pages_data[page_index])
                self.stacked_widget.addWidget(page)
                self.page_cache[page_index] = page  # 缓存加载过的页面
        self.stacked_widget.setCurrentIndex(page_index)

    def show_previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.load_page(self.current_page)  # 加载当前页
            self.update_buttons()

    def show_next_page(self):
        if self.current_page < len(self.pages_data) - 1:
            self.current_page += 1
            self.load_page(self.current_page)  # 加载下一页
            self.update_buttons()

    def update_buttons(self):
        self.prev_button.setEnabled(self.current_page > 0)
        self.next_button.setEnabled(self.current_page < len(self.pages_data) - 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
