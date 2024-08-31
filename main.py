# Import PySide6
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
)
from PySide6.QtCore import (
    QCoreApplication
)
from PySide6.QtCore import Qt
# Import Ui file from Qt Designer.
from PySide6.QtGui import QPixmap, QPainter
from app.modules.Ui_login import Ui_Form
from app.modules.Ui_registor import Ui_Registor
from app.modules.Ui_dialog import Ui_Dialog
from app.modules.Ui_main import Ui_mainWindow
# Import resources, sqlite3 tools and hashlib
import app.modules.assets.resources_rc
from app.database.tools import DatabaseTool
import hashlib
# Initialize the application
dbTool = DatabaseTool()
#TODO:move to lib
class DialogWindow(QDialog, Ui_Dialog):
    def __init__(self, title: str ,text: str):
        super().__init__()
        self.setupUi(self)        
        self.setWindowTitle(QCoreApplication.translate("Dialog", f"{title}", None))
        self.label.setText(QCoreApplication.translate("Dialog", f"{text}", None))

def openDialog(title: str, text: str):
    dialogWindow = DialogWindow(title, text)
    dialogWindow.exec()    
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
        username_input = self.username.text()
        password_input = self.password.text()
        if dbTool.user_exists(self.username.text()):
            if hashlib.sha256(
                    password_input.encode()
                ).hexdigest() == dbTool.query_user_password(username_input): 
                
                # self.msgBox("Login Success", f"Welcome! {self.username.text()}")
                openDialog("登入成功", f"{self.username.text()}，欢迎")
            else:
                openDialog("登入失败", "用户名或者密码错误\n请再试一次")
        else:
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

class ProfileWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        raise NotImplementedError
    
    
    
class MainWindow(QWidget, Ui_mainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Main Window")
        self.profile.clicked.connect(self.openProfile)
        # when content in lineEdit changed, call search function
        self.lineEdit.textChanged.connect(self.search)
        # TODO: add page of tabWeight
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/main.png")
        painter.drawPixmap(self.rect(), pixmap)
    
    def openProfile(self):
        # self.profileWindow = ProfileWindow()
        # self.profileWindow.show()
        raise NotImplementedError
    
    def search(self):
        raise NotImplementedError
        
        
class RegisterWindow(QWidget, Ui_Registor):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Register")
        # background = QPixmap(":/images/images/reg.png")
        # palette = QPalette()
        # palette.setBrush(QPalette.Window, QBrush(background))
        # self.setPalette(palette)
        self.register_btn.clicked.connect(self.register)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/reg.png")
        painter.drawPixmap(self.rect(), pixmap)
    
    def register(self) -> None:
        self._username = self.username.text()
        self.password_ipt = self.password.text()
        self.password2_ipt = self.password_2.text()
        if self._username == "" or self.password_ipt == "" or self.password2_ipt == "": 
            openDialog(title="提示", text="请输入完整信息")
        elif self.password_ipt == self.password2_ipt:
            dbTool.user_add(self._username, hashlib.sha256(self.password_ipt.encode()).hexdigest())
            openDialog(title="提示", text="注册成功")
            self.openMainWindow()
        else:
            openDialog(title="提示", text="两次输入的密码不一致")
        

    def openMainWindow(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.show()

if __name__ == "__main__":
    app = QApplication([])
    # apply_stylesheet(app, theme='dark_teal.xml')
    loginWindow = LoginWindow()
    loginWindow.show()
    app.exec()