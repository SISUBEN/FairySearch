from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox
)
from app.modules.Ui_login import Ui_Form
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
        # self.registerWindow = RegisterWindow()
        # self.registerWindo.show()

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("test")
        
class RegisterWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("test")

if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app, theme="dark_blue.xml")
    window = LoginWindow()
    window.show()
    app.exec()
