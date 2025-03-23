from app.__init__ import QApplication, QWidget, QPainter, QPixmap, logger
from app.modules.ui_login import Ui_Form
from app.database.queries import Database
from app.utils.crypto import CryptoHasher
from app.libs.register import RegisterWindow
from app.libs.main import MainWindow
from app.libs.dialog import Dialog
from app.i18n import _

class LoginWindow(QWidget, Ui_Form):
    def __init__(self, app: QApplication) -> None:
        super().__init__()
        
        self.app = app
        self.db = Database()
        self.cryptor = CryptoHasher()
        self.dialog = Dialog()
        
        self.setupUi(self)
        self.setWindowTitle(_("登录"))

        self.login_btn.clicked.connect(self.login)
        self.register_2.clicked.connect(self.openRegisterWindow)
        self.password.editingFinished.connect(self.login)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/background.png")
        painter.drawPixmap(self.rect(), pixmap)

    def login(self) -> None:
        username_input: str = self.username.text()
        password_input: str = self.password.text()
        enctrypt: str = self.cryptor.sha256(password_input)
        if self.db.userdb.is_user_exists(self.username.text()):
            logger.debug(f"user exists")
            if self.db.userdb.verify_user(username=username_input, password=enctrypt):
                logger.debug(f"verified scuccess")
                token = self.db.userdb.generate_token(
                    username=username_input, password=enctrypt
                )
                logger.debug(f"token: {token}")
                self.dialog.standardDialog(_("登入成功"), f"{self.username.text()}" + " " +_("欢迎") )
                self.openMainWindow(token)
            else:
                self.dialog.standardDialog(_("登入失败"), _("用户名或者密码错误\n请再试一次"))
        else:
            self.dialog.standardDialog(_("登入失败"), _("用户名或者密码错误\n请再试一次"))

    def openRegisterWindow(self) -> None:
        # self.close()
        # hide login window
        self.registerWindow = RegisterWindow(self) # pass self to register window
        self.registerWindow.show()
        self.hide()

    def openMainWindow(self, token: str) -> None:
        self.close()
        self.mainWindow = MainWindow(token, self.app)
        self.mainWindow.show()
