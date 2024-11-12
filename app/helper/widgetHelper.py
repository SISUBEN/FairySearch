import uuid
from PySide6.QtWidgets import (
    QPushButton,
    QLabel,
    QLineEdit,
    QComboBox
)
# from PySide6.QtGui import *
# from PySide6.QtCore import *

class WidgetHelper(object):
    def __init__(self) -> None:
        ...

    def creatLink(self, content: str, color: str = "white") -> QPushButton:
        """Create a link-like button

        Args:
            content (str): the content of the button
            target (callable): the function to be called when the button is clicked

        Returns:
            QPushButton: return a QPushButton object
        """
        assert isinstance(content, str), "content must be a string"
        self.link_like_btn = QPushButton()
        link_id = str(uuid.uuid4())
        self.link_like_btn.setObjectName(f"link_like_btn_{link_id}")
        self.link_like_btn.setStyleSheet("QPushButton#link_like_btn_"+link_id+" {" 
        "	color: #1a0dab;\n"
        f"	color: {color};\n"
        "	background-color:transparent;\n"
        "   text-align: center;\n"
        "}\n"   
        "QPushButton#link_like_btn_"+link_id+":pressed {\n"
        "	color: #681DA8;\n"
        "	background-color:transparent;\n"
        "   text-align: center;\n"
        "}\n"
        "QPushButton#link_like_btn_"+link_id+":hover {\n"
        "	text-decoration: underline;\n"
        "	background-color:transparent;\n"
        "   text-align: center;\n"
        "}")
        self.link_like_btn.setText(content)
        # self.link_like_btn.clicked.connect(target)
        return self.link_like_btn

    def createLabel(self, text: str, size: int, color: str) -> QLabel:
        ...

    def createButton(self, text: str, size: int, color: str) -> QPushButton:
        ...

    def createLineEdit(self, placeholder: str, size: int, color: str) -> QLineEdit:
        ...

    def createComboBox(self, size: int, color: str) -> QComboBox:
        ...