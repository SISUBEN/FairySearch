from app.__init__ import *
from app.modules.Ui_login import Ui_Form
from app.database.queries import Database
from app.utils.crypto import CryptoHasher

from app.libs.register import RegisterWindow
from app.libs.main import MainWindow
from app.libs.dialog import openDialog

db = Database()
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
        username_input: str = self.username.text()
        password_input: str = self.password.text()
        enctrypt: str = cryptor.sha256(password_input)
        if db.userdb.user_exists(self.username.text()):
            logger.debug(f"user exists")
            logger.debug(f"username: {username_input}, password: {password_input}")
            if db.userdb.verify_user(username=username_input, password=enctrypt):
                logger.debug(f"verified scuccess")
                token = db.userdb.generate_token(username=username_input, password=enctrypt)
                logger.debug(f"token: {token}")
                openDialog("登入成功", f"{self.username.text()}，欢迎")
                self.openMainWindow(token)
            else:
                openDialog("登入失败", "用户名或者密码错误\n请再试一次")
        else:
            openDialog("登入失败", "用户不存在")

    def register(self) -> None:
        self.close()
        self.registerWindow = RegisterWindow()
        self.registerWindow.show()

    def openMainWindow(self, token: str) -> None:
        self.close()
        self.mainWindow = MainWindow(token)
        self.mainWindow.show()

    def openRegisterWindow(self) -> None:
        self.close()
        self.registerWindow = RegisterWindow()
        self.registerWindow.show()
