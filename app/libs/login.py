from app.__init__ import *
from app.modules.Ui_login import Ui_Form
from app.database.queries import Database
from app.utils.crypto import CryptoHasher

from app.libs.register import RegisterWindow
from app.libs.main import MainWindow
from app.libs.dialog import openDialog
from app.libs.status import Status

status = Status
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
        username_input: str = self.username.text()
        password_input: str = self.password.text()
        enctrypt: str = cryptor.sha256(password_input)
        if db.userdb.user_exists(self.username.text()):
            if db.userdb.verify_user(username_input, enctrypt):
                token = db.userdb.generate_token(enctrypt)
                status.set_login()
                logger.debug(f"token: {token}")
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
