from app.__init__ import *
from app.modules.Ui_registor import Ui_Registor
from app.database.queries import Database
from app.utils.crypto import CryptoHasher
from app.utils.validator import Password, Username
from app.libs.main import MainWindow
from app.libs.dialog import openDialog

db = Database()
cryptor = CryptoHasher()
passwd_val = Password()
usrname_val = Username()


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
            # db.userdb.user_add(
            #     self._username, cryptor.sha256(self.password_ipt)
            # )
            # encyted = cryptor.sha256(self.password_ipt)
            db.userdb.t_user_add(self._username, self.password_ipt)
            openDialog(title="提示", text="注册成功")
            self.openMainWindow()
        elif not usrname_val.validate(self._username):
            openDialog(
                title="提示",
                text="用户名格式不正确\n字母开头，长度5-16个字，字母数字下划线组合",
            )
        elif not passwd_val.validate(self.password_ipt):
            openDialog(
                title="提示",
                text="密码格式不正确\n必须包含大小写字母和数字的组合，可以使用特殊字符，长度在8-10之间",
            )
        else:
            openDialog(title="提示", text="两次输入的密码不一致")

    def openMainWindow(self) -> None:
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.show()
