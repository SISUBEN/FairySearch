from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox
)
from app.modules.Ui_login import Ui_Form
# from app.modules.Ui_register import Ui_Register
from app.modules.Ui_reg import Ui_Reg as Ui_Register
from app.assets.resources_rc import *
from app.database.tools import DatabaseTool
import hashlib
from qt_material import apply_stylesheet
dbTool = DatabaseTool()
class LoginWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.login)
        self.register_2.clicked.connect(self.register)
    def login(self):
        username_input = self.username.text()
        password_input = self.password.text()
        if dbTool.user_exists(self.username.text()):
            if hashlib.sha256(
                    password_input.encode()
                ).hexdigest() == dbTool.query_user_password(username_input): 
                self.msgBox("Login Success", f"Welcome! {self.username.text()}")
            else:
                self.msgBox("Login Fail", "Username or password incorrect!\nPlease try again.")
        else:
            self.msgBox("Login Fail", "User does not exist!")
            
    def msgBox(self, title:str, text: str):
        MessageBox = QMessageBox()
        MessageBox.about(self, title, text)
        
    def register(self):
        pass
    
    def openMainWindow(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        
    def openRegisterWindow(self):
        self.close()
        self.registerWindow = RegisterWindow()
        self.registerWindow.show()

class MainWindow(QWidget):
    def __init__(self) -> None:
        # TODO: 实现mainwindow
        super().__init__()
        self.setWindowTitle("test")
        
class RegisterWindow(QWidget, Ui_Register, LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_btn.clicked.connect(self.register)
    
    def register(self) -> None:
        self.username = self.username.text()
        self.password_ipt = self.password.text()
        self.password2_ipt = self.password_2.text()
        if self.password_ipt == self.password2_ipt:
            dbTool.user_add(self.username, hashlib.sha256(self.password_ipt.encode()).hexdigest())
            self.msgBox("Register Success", "Register Success!")
        else:
            self.msgBox("Register Fail", "Password not match!")
        self.openMainWindow()

if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app, theme="dark_blue.xml")
    window = LoginWindow()
    window.show()
    app.exec()
