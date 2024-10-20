# Import PySide6
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
)
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap, QPainter
# Import Ui file from Qt Designer.

from app.modules.Ui_login import Ui_Form
from app.modules.Ui_registor import Ui_Registor
from app.modules.Ui_dialog import Ui_Dialog
from app.modules.Ui_main import Ui_MainWindow, ItemWidget, PageWidget
from app.modules.Ui_profile import Ui_Profile

# Import resources, utils and libs
import app.modules.assets.resources_rc
from app.database.queries import Database
from app.utils.crypto import CryptoHasher
from app.utils.validator import (
    Password, Username
)
from loguru import logger

# Initialize the application
db = Database
passwd_val = Password()
usrname_val = Username()
cryptor = CryptoHasher
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
    def __init__(self, title: str, text: str) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(QCoreApplication.translate(
            "Dialog", f"{title}", None))
        self.label.setText(QCoreApplication.translate(
            "Dialog", f"{text}", None))

def openDialog(title: str, text: str) -> None:
    dialogWindow = DialogWindow(title, text)
    dialogWindow.exec()


class MainWindow(
    QWidget,
    Ui_MainWindow,
):
    def __init__(self) -> None:
        super().__init__()
        self.bg_image_path = ":/images/images/background.png"  # using QRC path
        self.def_cover_path = ":/covers/covers/default.png"  # using QRC path
        self.pages_data = [
            [
                {"cover": self.def_cover_path, "title": "Item 1"},
                {"cover": self.def_cover_path, "title": "Item 2"},
                {"cover": self.def_cover_path, "title": "Item 3"},
                {"cover": self.def_cover_path, "title": "Item 4"},
                {"cover": self.def_cover_path, "title": "Item 5"},
                {"cover": self.def_cover_path, "title": "Item 6"},
            ],
        ]
        self.setupUi(self, self.pages_data)
        
        # bind button click events
        self.prev_button.clicked.connect(self.show_prev_page)
        self.next_button.clicked.connect(self.show_next_page)
        self.page_number.editingFinished.connect(self.jump_to_page)
        self.user_profile_btn.clicked.connect(self.show_user_profile)
        self.update_buttons()
        
    def append_page(self, *items_data: list) -> None:
        for data in items_data:
            self.pages_data.append(data)
            self.load_page(len(self.pages_data) - 1)
            self.update_buttons()

    def paintEvent(self, event) -> None:
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

    def show_user_profile(self) -> None:
        self.profileWindow = ProfileWindow()
        self.profileWindow.show()

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
        self.next_button.setEnabled(
            self.current_page < len(self.pages_data) - 1)


class LoginWindow(QWidget, Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.login)
        self.register_2.clicked.connect(self.register)
        self.password.editingFinished.connect(self.login)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/background.png")
        painter.drawPixmap(self.rect(), pixmap)

    def login(self) -> None:
        global LOGIN
        username_input = self.username.text()
        password_input = self.password.text()
        if db.userdb.user_exists(self.username.text()):
            if (
                cryptor.encrypt_sha256(password_input)
                == db.userdb.query_user_password(username_input)[0][0]
            ):
                LOGIN = username_input
                openDialog("登入成功", f"{self.username.text()}，欢迎")
                self.openMainWindow()
            else:
                openDialog("登入失败", "用户名或者密码错误\n请再试一次")
        else:
            openDialog("登入失败", "用户不存在")

    def register(self) -> None:
        self.close()
        self.registerWindow = RegisterWindow()
        self.registerWindow.show()

    def openMainWindow(self) -> None:
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.show()

    def openRegisterWindow(self) -> None:
        self.close()
        self.registerWindow = RegisterWindow()
        self.registerWindow.show()

class ProfileWindow(QWidget, Ui_Profile):
    def __init__(self) -> None:
        super().__init__()
        _uid = str(db.userdb.query_user_uid(LOGIN)[0][0])
        self.setupUi(self, LOGIN, _uid)
        # disable zoom
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("Profile")
        logger.debug(f"var -> LOGIN => {LOGIN}")
        logger.debug(
            f"client -> userdb [GET] db.userdb.query_user_uid(LOGIN)[0] => {db.userdb.query_user_uid(LOGIN)[0]}"
        )
        # init search history
        self.tableWidget.setHorizontalHeaderLabels(["标题", "浏览时间", "时长"])
        
        # bind slot
        self.onSearchHistory()
        self.changeAvatar.clicked.connect(self.onChangeAvatar)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/profile.png")
        painter.drawPixmap(self.rect(), pixmap)
    
    def addSearchHistory(self, item: ItemWidget) -> None:
        pass
    
    def onSearchHistory(self) -> None:
        pass

    def onChangeAvatar(self) -> None:
        pass


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
        elif self.password_ipt == self.password2_ipt:
            db.userdb.user_add(
                self._username, cryptor.encrypt_sha256(self.password_ipt)
            )
            openDialog(title="提示", text="注册成功")
            self.openMainWindow()
        elif not usrname_val.validate(self._username):
            openDialog(title="提示", text="用户名格式不正确\n字母开头，长度5-16个字，字母数字下划线组合")
        elif not passwd_val.validate(self.password_ipt):
            openDialog(title="提示", text="密码格式不正确\n必须包含大小写字母和数字的组合，可以使用特殊字符，长度在8-10之间")
        else:
            openDialog(title="提示", text="两次输入的密码不一致")

    def openMainWindow(self) -> None:
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
        logger.critical(
            f"An error occurred while the program was running: {err}")
        app.shutdown()
    except KeyboardInterrupt:
        logger.error("The program was interrupted by the user")
        app.shutdown()
