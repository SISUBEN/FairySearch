from app.__init__ import *
from app.modules.ui_registor import Ui_Registor
from app.database.queries import Database
from app.utils.crypto import CryptoHasher
from app.utils.validator import Password, Username
from app.libs.main import MainWindow
# from app.libs.main import 
from app.libs.expection import NoLoginError
from app.libs.dialog import Dialog
dialog = Dialog()
from app.i18n import _

db = Database()
cryptor = CryptoHasher()
passwd_val = Password()
usrname_val = Username()


class RegisterWindow(QWidget, Ui_Registor):
    def __init__(self, login_window: object) -> None:
        super().__init__()
        self.login_window = login_window
        self.setupUi(self)
        self.setWindowTitle(_("注册"))
        self.__token = None
        self.register_btn.clicked.connect(self.register)
        self.back.clicked.connect(self.openLoginWindow)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/reg.png")
        painter.drawPixmap(self.rect(), pixmap)

    def register(self) -> None:
        self._username = self.username.text()
        self.password_ipt = self.password.text()
        self.password2_ipt = self.password_2.text()
        if db.userdb.is_user_exists(self._username):
            dialog.standardDialog(title=_("提示"), text=_("用户名已存在"))
        elif self.password_ipt == self.password2_ipt:
            # db.userdb.user_add(
            #     self._username, cryptor.sha256(self.password_ipt)
            # )
            # encyted = cryptor.sha256(self.password_ipt)
            self.__token = db.userdb.t_user_add(self._username, self.password_ipt)
            dialog.standardDialog(title=_("提示"), text=_("注册成功"))
            self.openMainWindow()
        elif not usrname_val.validate(self._username):
            dialog.standardDialog(
                title=_("提示"),
                text=_("用户名格式不正确\n字母开头，长度5-16个字，字母数字下划线组合"),
            )
        elif not passwd_val.validate(self.password_ipt):
            dialog.standardDialog(
                title=_("提示"),
                text=_("密码格式不正确\n必须包含大小写字母和数字的组合，可以使用特殊字符，长度在8-10之间"),
            )
        else:
            dialog.standardDialog(title=_("提示"), text=_("两次输入的密码不一致"))
            
    def openLoginWindow(self) -> None:
        self.close()
        self.login_window.show()
        
    def openMainWindow(self) -> None:
        self.close()
        try:
            self.mainWindow = MainWindow(token=self.__token)
        except NoLoginError:
            logger.log("user not login, back to [login.py] page")
            dialog.standardDialog(_("提示"), _("请先登录"))
        self.mainWindow.show()
