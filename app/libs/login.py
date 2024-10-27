from app.__init__ import *
from app.modules.Ui_login import Ui_Form
from app.database.queries import Database
from app.utils.crypto import CryptoHasher

from app.libs.register import RegisterWindow
from app.libs.main import MainWindow
from app.libs.dialog import openDialog

db = Database
cryptor = CryptoHasher()


class LoginWindow(QWidget, Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("登录")

        self.login_btn.clicked.connect(self.login)
        self.register_2.clicked.connect(self.register)
        self.password.editingFinished.connect(self.login)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/background.png")
        painter.drawPixmap(self.rect(), pixmap)

    def login(self) -> None:
        global LOGIN, LOGIN_UID
        username_input: str = self.username.text()
        password_input: str = self.password.text()
        if db.userdb.user_exists(self.username.text()):
            logger.debug(
                f"password type: {type(password_input)}\n\t=> {password_input}"
            )
            if (
                cryptor.encrypt_sha256(string=password_input)
                == db.userdb.query_user_password(username_input)[0][0]
            ):
                LOGIN = username_input
                LOGIN_UID = str(db.userdb.query_user_uid(LOGIN)[0][0])
                logger.debug(f"login: {LOGIN}\n\tlogin uid: {LOGIN_UID}")
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
