from PySide6.QtWidgets import QApplication, QWidget
from Ui_login import Ui_Form
class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        
    # def login(self):
    #     if self.lineEdit == "admin" and self.lineEdit_2 == "123456":
            
    # 登入函数
    
            
            
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
