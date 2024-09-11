from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt
class PagedWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("翻页效果示例")

        # 当前页码
        self.current_page = 0
        
        # 设置中央窗口部件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # 主布局
        self.main_layout = QVBoxLayout(self.central_widget)

        # 显示内容的布局（每页的内容）
        self.content_layout = QVBoxLayout()

        # 添加翻页按钮
        self.page_buttons_layout = QHBoxLayout()
        self.prev_button = QPushButton("上一页")
        self.next_button = QPushButton("下一页")
        self.page_buttons_layout.addWidget(self.prev_button)
        self.page_buttons_layout.addWidget(self.next_button)

        # 连接翻页按钮的信号
        self.prev_button.clicked.connect(self.prev_page)
        self.next_button.clicked.connect(self.next_page)

        # 添加内容布局和翻页按钮到主布局
        self.main_layout.addLayout(self.content_layout)
        self.main_layout.addLayout(self.page_buttons_layout)

        # 初始化第一页的内容
        self.load_page(self.current_page)

    def load_page(self, page_number):
        """加载指定页码的内容"""
        # 清空当前的内容
        self.clear_layout(self.content_layout)

        # 根据页码加载不同的内容
        if page_number == 0:
            label = QLabel("这是第一页的内容")
        elif page_number == 1:
            label = QLabel("这是第二页的内容")
        elif page_number == 2:
            label = QLabel("这是第三页的内容")
        else:
            label = QLabel("这是默认页内容")

        # 添加内容到布局
        label.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(label)

        # 更新按钮状态
        self.update_buttons()

    def clear_layout(self, layout):
        """清空布局中的所有控件"""
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def prev_page(self):
        """跳转到上一页"""
        if self.current_page > 0:
            self.current_page -= 1
            self.load_page(self.current_page)

    def next_page(self):
        """跳转到下一页"""
        self.current_page += 1
        self.load_page(self.current_page)

    def update_buttons(self):
        """更新按钮的状态，禁用无效的翻页按钮"""
        self.prev_button.setEnabled(self.current_page > 0)
        self.next_button.setEnabled(self.current_page < 2)  # 假设有 3 页

if __name__ == "__main__":
    app = QApplication([])

    window = PagedWindow()
    window.show()

    app.exec()