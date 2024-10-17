from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget,
    QGridLayout,
)
from PySide6.QtGui import QPixmap
import sys


class ItemWidget(QWidget):
    def __init__(self, cover_image_path, title, *args, **kwargs):
        super(ItemWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout()

        # 封面图片
        self.cover_label = QLabel(self)
        pixmap = QPixmap(cover_image_path)
        self.cover_label.setPixmap(pixmap)
        self.cover_label.setScaledContents(True)
        self.cover_label.setFixedSize(600, 550)  # 设置封面大小
        layout.addWidget(self.cover_label)

        # 标题
        self.title_label = QLabel(title, self)
        layout.addWidget(self.title_label)

        self.setLayout(layout)


class PageWidget(QWidget):
    def __init__(self, items_data, *args, **kwargs):
        super(PageWidget, self).__init__(*args, **kwargs)
        layout = QGridLayout()  # 使用网格布局来安排6个项目
        for i, item_data in enumerate(items_data):
            item = ItemWidget(item_data["cover"], item_data["title"])
            layout.addWidget(item, i // 3, i % 3)  # 3列布局
        self.setLayout(layout)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("翻页程序")

        # 主布局
        main_layout = QVBoxLayout(self)

        # 翻页内容部分
        self.stacked_widget = QStackedWidget(self)

        # 假设有两页内容，每页6个项目
        pages_data = [
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
        ]

        for page_data in pages_data:
            page = PageWidget(page_data)
            self.stacked_widget.addWidget(page)
        main_layout.addWidget(self.stacked_widget)

        # 翻页按钮布局
        button_layout = QHBoxLayout()
        self.prev_button = QPushButton("上一页", self)
        self.next_button = QPushButton("下一页", self)
        self.prev_button.clicked.connect(self.show_previous_page)
        self.next_button.clicked.connect(self.show_next_page)

        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)
        main_layout.addLayout(button_layout)

        self.current_page = 0
        self.update_buttons()

    def show_previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.stacked_widget.setCurrentIndex(self.current_page)
            self.update_buttons()

    def show_next_page(self):
        if self.current_page < self.stacked_widget.count() - 1:
            self.current_page += 1
            self.stacked_widget.setCurrentIndex(self.current_page)
            self.update_buttons()

    def update_buttons(self):
        self.prev_button.setEnabled(self.current_page > 0)
        self.next_button.setEnabled(self.current_page < self.stacked_widget.count() - 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 600)
    window.show()
    sys.exit(app.exec())
