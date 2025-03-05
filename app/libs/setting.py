from app.__init__ import *
from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget, QComboBox
from PySide6.QtGui import QIcon, QFont
from app.modules.ui_setting import Ui_SettingWindow
from app.i18n import _
import time 

class SettingWindow(QWidget, Ui_SettingWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(_('设置'))
        self.a = self.addSetting()
    
    def addSetting(
        self,
        title: QWidget,
        content: QWidget,           
    ) -> None:
        pass