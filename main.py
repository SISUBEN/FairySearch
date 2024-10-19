# Import PySide6
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
    QLabel,
)
from PySide6.QtCore import QCoreApplication

# Import Ui file from Qt Designer.
from PySide6.QtGui import QPixmap, QPainter
from app.modules.Ui_login import Ui_Form
from app.modules.Ui_registor import Ui_Registor
from app.modules.Ui_dialog import Ui_Dialog

# from app.modules.Ui_main_deprecated import Ui_MainWindow
from app.modules.Ui_main import Ui_MainWindow, ItemWidget, PageWidget
from app.modules.Ui_profile import Ui_Profile

# Import resources, sqlite3 tools, hashlib and loguru
import app.modules.assets.resources_rc
from app.database.queries import Database
import hashlib
from loguru import logger

# Initialize the application
db = Database
LOGIN = None  # TODO: use token to save login status
# logger.add(
#     "logs/main_{time}.log",
#     rotation="1 MB",
#     retention="10 days",
#     level="WARNING",
#     encoding='utf-8',
#     backtrace=True,
#     diagnose=True,
# )
logger.success("Fairy Search initialize successfully")


# TODO:move to lib
class DialogWindow(QDialog, Ui_Dialog):
    def __init__(self, title: str, text: str):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(QCoreApplication.translate("Dialog", f"{title}", None))
        self.label.setText(QCoreApplication.translate("Dialog", f"{text}", None))


def openDialog(title: str, text: str):
    dialogWindow = DialogWindow(title, text)
    dialogWindow.exec()


class MainWindow(
    QWidget,
    Ui_MainWindow,
):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # bind button click events
        self.prev_button.clicked.connect(self.show_prev_page)
        self.next_button.clicked.connect(self.show_next_page)
        self.page_number.editingFinished.connect(self.jump_to_page)
        self.user_profile_btn.clicked.connect(self.show_user_profile)
        self.update_buttons()

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
        profileWindow = ProfileWindow()
        profileWindow.show()

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


class LoginWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.login)
        self.register_2.clicked.connect(self.register)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/background.png")
        painter.drawPixmap(self.rect(), pixmap)

    def login(self):
        global LOGIN
        username_input = self.username.text()
        password_input = self.password.text()
        logger.info(f"username: {username_input}, password: {password_input}")
        logger.debug(
            f"client -> userdb [GET] db.userdb.user_exists(self.username.text()) => {db.userdb.user_exists(self.username.text())}"
        )
        if db.userdb.user_exists(self.username.text()):
            logger.info(f"User {username_input} is trying to login")
            logger.debug(
                f"""client -> userdb [GET] hashlib.sha256(
                password_input.encode()
            ).hexdigest() == db.userdb.query_user_password(username_input) => {hashlib.sha256(
                password_input.encode()
            ).hexdigest() == db.userdb.query_user_password(username_input)}\ninputed password: {hashlib.sha256(
                password_input.encode()
            ).hexdigest()}\nhashed password: {db.userdb.query_user_password(username_input)}"""
            )

            if (
                hashlib.sha256(password_input.encode()).hexdigest()
                == db.userdb.query_user_password(username_input)[0][0]
            ):
                LOGIN = username_input
                logger.success(f"User {username_input} login successfully")
                openDialog("登入成功", f"{self.username.text()}，欢迎")
                self.openMainWindow()
            else:
                logger.info(f"User {username_input} login failed")
                openDialog("登入失败", "用户名或者密码错误\n请再试一次")
        else:
            logger.info(f"User {username_input} is not exists")
            openDialog("登入失败", "用户不存在")

    def register(self):
        self.close()
        self.registerWindow = RegisterWindow()
        self.registerWindow.show()

    def openMainWindow(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.show()

    def openRegisterWindow(self):
        self.close()
        self.registerWindow = RegisterWindow()
        self.registerWindow.show()


class ProfileWindow(QWidget, Ui_Profile):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Profile")
        logger.debug(f"var -> LOGIN => {LOGIN}")
        self.username.setText(self.username.text().replace("$username$", LOGIN))
        self.uid.setText(
            self.uid.text().replace(
                # select the first row of the first column of the table
                "$uid$",
                str(db.userdb.query_user_uid(LOGIN)[0][0]),
            )
        )
        logger.debug(
            f"client -> userdb [GET] db.userdb.query_user_uid(LOGIN)[0] => {db.userdb.query_user_uid(LOGIN)[0]}"
        )
        self.onSearchHistory()
        self.changeAvatar.clicked.connect(self.onChangeAvatar)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/profile.png")
        painter.drawPixmap(self.rect(), pixmap)

    def onSearchHistory(self):
        pass

    def onChangeAvatar(self):
        pass

# this class has been decprecated, but im not sure what will happen after remove 
# class MainWindow(QWidget, Ui_MainWindow):
#     def __init__(self) -> None:
#         super().__init__()
#         self.window = None
#         self.setupUi(self)
#         self.setWindowTitle("Main Window")
#         self.profile_btn.clicked.connect(self.openProfile)
#         self.current_page: int = 1
#         self.total_pages: int = db.videodb.count_videos()
#         # when content in lineEdit changed, call search function
#         self.search_box.returnPressed.connect(self.search)
#         # TODO: add page of tabWeight
#         self.prev_page_btn.clicked.connect(self.prevPage)
#         self.next_page_btn.clicked.connect(self.nextPage)
#         # 按下回车跳转到对应页数
#         self.page_num.returnPressed.connect(self.gotoPage)

#     def clearLayout(self, layout):
#         """清空布局中的所有控件"""
#         while layout.count():
#             child = layout.takeAt(0)
#             if child.widget():
#                 child.widget().deleteLater()

#     def loadPage(self, page_num):
#         """加载指定页码的内容"""
#         # 清空当前的内容
#         self.clearLayout(self.gridLayout_3)
#         # label = QLabel("这是第一页的内容")
#         # self.gridLayout_3.addWidget(label)
#         # 获取指定页码的内容
#         videos = db.videodb.query_videos_by_page(page_num, 10)
#         # 将内容添加到布局中
#         for i, video in enumerate(videos):
#             # 创建一个QLabel来显示视频信息
#             label = QLabel(video[1])
#             # 设置标签的样式
#             label.setStyleSheet("font-size: 20px; color: white;")
#             # 将标签添加到布局中
#             self.gridLayout_3.addWidget(label, i, 0)
#             # 创建一个QLabel来显示视频封面
#             cover_label = QLabel()
#             # 设置标签的样式
#             cover_label.setStyleSheet("border: 1px solid black;")
#             # 加载视频封面图片
#             cover_label.setPixmap(QPixmap(video[2]))
#             # 将标签添加到布局中
#             self.gridLayout_3.addWidget(cover_label, i, 1)

#     def prevPage(self):
#         """上一页"""
#         if self.current_page > 1:
#             self.current_page -= 1
#             self.loadPage(self.current_page)
#             self.updateButtons()
#             # 更新页码显示
#             self.page_num.setText(str(self.current_page))

#     def nextPage(self):
#         """下一页"""
#         if self.current_page < self.total_pages:
#             self.current_page += 1
#             self.loadPage(self.current_page)
#             self.updateButtons()
#             self.page_num.setText(str(self.current_page))

#     def gotoPage(self):
#         """跳转到指定页数"""
#         page_num = int(self.page_num.text())
#         if 1 <= page_num <= self.total_pages:
#             self.current_page = page_num
#             self.loadPage(self.current_page)
#             self.updateButtons()

#     def updateButtons(self):
#         """更新按钮的状态，禁用无效的翻页按钮"""
#         self.prev_page_btn.setEnabled(self.current_page > 0)
#         self.next_page_btn.setEnabled(self.current_page < self.total_pages)

#     def openProfile(self):
#         self.profileWindow = ProfileWindow()
#         self.profileWindow.show()

#     def search(self):
#         raise NotImplementedError

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.drawRect(self.rect())
#         pixmap = QPixmap(":/images/images/background.png")
#         painter.drawPixmap(self.rect(), pixmap)

class RegisterWindow(QWidget, Ui_Registor):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("注册")
        self.register_btn.clicked.connect(self.register)
        self.back.clicked.connect(self.openMainWindow)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/reg.png")
        painter.drawPixmap(self.rect(), pixmap)

    def register(self) -> None:
        self._username = self.username.text()
        self.password_ipt = self.password.text()
        self.password2_ipt = self.password_2.text()
        if db.userdb.user_exists(self._username):
            openDialog(title="提示", text="用户名已存在")
        elif (
            self._username == "" or self.password_ipt == "" or self.password2_ipt == ""
        ):
            openDialog(title="提示", text="请输入完整信息")
        elif self.password_ipt == self.password2_ipt:
            db.userdb.user_add(
                self._username, hashlib.sha256(self.password_ipt.encode()).hexdigest()
            )
            openDialog(title="提示", text="注册成功")
            self.openMainWindow()
        else:
            openDialog(title="提示", text="两次输入的密码不一致")

    def openMainWindow(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.show()


if __name__ == "__main__":
    try:
        app = QApplication([])
        loginWindow = LoginWindow()
        loginWindow.show()
        app.exec()
    except Exception as err:
        logger.critical(f"An error occurred while the program was running: {err}")
        app.shutdown()
    except KeyboardInterrupt:
        logger.error("The program was interrupted by the user")
        app.shutdown()
