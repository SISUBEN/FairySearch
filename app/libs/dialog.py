from app.modules.ui_dialog import Ui_Dialog
from app import QCoreApplication, QDialog

class DialogWindow(QDialog, Ui_Dialog):
    def __init__(self, title: str, text: str) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(QCoreApplication.translate(
            "Dialog", f"{title}", None))
        self.label.setText(QCoreApplication.translate(
            "Dialog", f"{text}", None))
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.close)

class Dialog:
    @staticmethod
    def standard(title: str, text: str) -> None:
        dialogWindow = DialogWindow(title, text)
        dialogWindow.exec()
        return dialogWindow

    