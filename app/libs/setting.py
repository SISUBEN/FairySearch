from app.__init__ import QApplication
from app.assets.resource_manager import ResourceManager
from PySide6.QtWidgets import QLabel, QHBoxLayout, QWidget
from PySide6.QtCore import QTranslator
from PySide6.QtGui import QFont
from app.utils.logger.logger import logger
from app.helper.widget import WidgetCreator
from app.assets.config import LanguageSerializer, Language
from app.modules.ui_setting import Ui_SettingWindow
from app.i18n import _, t
from app.assets.config import cfg
import logging
serializer = LanguageSerializer()
creator = WidgetCreator()
class SettingWindow(QWidget, Ui_SettingWindow):
    def __init__(self, app: QApplication) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(_('设置'))
        # TODO: promote to qfluentwidgets
        self.app = app
        self.rm = ResourceManager(app)
        self.support_lang = ["English", "中文", "繁體中文"]
        self.lang_combo_box = creator.createComboBox(self.support_lang)
        self.current_lang = cfg.load("language")
        self.lang_combo_box.setCurrentIndex()
        self.log_level_combo_box = creator.createComboBox(["DEBUG", "INFO"])
        
        self.addSetting("langVLayout", QLabel(_("界面语言：")), self.lang_combo_box)
        self.addSetting("devVLayout", QLabel(_("日志等级：")), self.log_level_combo_box)

        self.log_level_combo_box.currentIndexChanged.connect(self.onChangeLogLevel)
        self.lang_combo_box.currentIndexChanged.connect(self.onChangeLang)

    def addSetting(
        self,
        parent_setting_layout: str,
        title: QWidget,
        content: QWidget,
    ) -> None:
        """
        Adds a setting to the specified parent layout.
        Args:
            parent_setting_layout (str): The name of the parent layout attribute.
            title (QWidget): The title widget to be added.
            content (QWidget): The content widget to be added.
        Returns:
            None
        """
        layout = getattr(self, parent_setting_layout, None)
        if layout is not None:
            h_layout = QHBoxLayout()
            title.setFont(QFont("Microsoft YaHei", 12, QFont.Bold))
            content.setFont(QFont("Microsoft YaHei", 12))
            h_layout.addWidget(title)
            content.setMaximumWidth(200)
            h_layout.addWidget(content)
            layout.addLayout(h_layout)
    
    def onChangeLogLevel(self, index: int) -> None:
        if index == 0:
            logger.setLevel(logging.DEBUG)
            cfg.set("log_level", "DEBUG")
        elif index == 1:
            logger.setLevel(logging.INFO)
            cfg.set("log_level", "INFO")
            
    def onChangeLang(self, index: int) -> None:
        serializer.serialize(Language.AUTO)
        if index == 0:
            lang = serializer.serialize(Language.ENGLISH)
        elif index == 1:
            lang = serializer.serialize(Language.SIMP_CHINESE)
        elif index == 2:
            lang = serializer.serialize(Language.TRA_CHINESE)
            logger.debug(f"Change language to {lang}")
        _translator = self.rm.getTranslator(lang)
        self._load_translation(_translator, lang)
        self.retranslateUi(self)
            
    def _load_translation(self, translator: QTranslator, language: str) -> None:
        t.set_language(language)
        cfg.set("language", language)
        translator.load(f":/i18n/{language}.qm")
        self.rm.setTranslation(language)