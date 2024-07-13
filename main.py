from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox
)
from PySide6.QtCore import (
    Signal,
    Qt
)
from app.modules.Ui_login import Ui_Form
from app.assets.resources_rc import *
from qt_material import apply_stylesheet
class MainWindow(QWidget, Ui_Form):
    clicked = Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.login)
        self.register_2.clicked.connect(self.register_2)
        
    def login(self):
        if self.username.text() == "admin" and self.password.text() == "123456":
            self.msgBox("Login Success", f"Welcome! {self.username.text()}")
        else:
            self.msgBox("Login Fail", "Username or password incorrect!\nPlease try again.")
    def msgBox(self, title:str, text: str):
        MessageBox = QMessageBox()
        MessageBox.about(self, title, text)
        
    def register():
        pass
    
if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
    window = MainWindow()
    window.show()
    app.exec()
