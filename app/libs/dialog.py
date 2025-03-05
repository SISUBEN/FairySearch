from app.modules.ui_dialog import Ui_Dialog
from app.__init__ import *

class DialogWindow(QDialog, Ui_Dialog):
    def __init__(self, title: str, text: str) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(QCoreApplication.translate(
            "Dialog", f"{title}", None))
        self.label.setText(QCoreApplication.translate(
            "Dialog", f"{text}", None))

def openDialog(title: str, text: str) -> None:
    dialogWindow = DialogWindow(title, text)
    dialogWindow.exec()
    