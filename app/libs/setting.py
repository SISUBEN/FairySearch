from app.__init__ import *
from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget, QComboBox
from PySide6.QtGui import QFont
from app.modules.ui_setting import Ui_SettingWindow
from app.i18n import _

class SettingWindow(QWidget, Ui_SettingWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(_('设置'))
        
        self.lang_combo_box = QComboBox()
        self.lang_combo_box.addItems(["English", "中文", "繁體中文"])
        self.addSetting("langVLayout", QLabel(_("界面语言：")), self.lang_combo_box)
        
        self.log_level_combo_box = QComboBox()
        self.log_level_combo_box.addItems(["DEBUG", "INFO"])
        self.addSetting("devVLayout", QLabel(_("日志等级：")), self.log_level_combo_box)

        self.log_level_combo_box.currentIndexChanged.connect(self.onChangeLogLevel)
        self.lang_combo_box.currentIndexChanged.connect(self.onChangeLang)

    
    def addSetting(
        self,
        parent_setting_layout: str,
        title: QWidget,
        content: QWidget,         
    ) -> None:
        layout = getattr(self, parent_setting_layout, None)
        if layout is not None:
            h_layout = QHBoxLayout()
            title.setFont(QFont("Microsoft YaHei", 12, QFont.Bold))
            content.setFont(QFont("Microsoft YaHei", 12))
            h_layout.addWidget(title)
            content.setMaximumWidth(200)
            h_layout.addWidget(content)
            layout.addLayout(h_layout)