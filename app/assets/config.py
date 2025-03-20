from enum import Enum
from PySide6.QtCore import QLocale, Qt
import logging
from qfluentwidgets import QConfig, ConfigItem, BoolValidator, ConfigSerializer, qconfig, OptionsConfigItem, OptionsValidator

class Language(Enum):
    """ Language enumeration class """

    SIMP_CHINESE = QLocale(QLocale.Chinese, QLocale.China)
    TRA_CHINESE = QLocale(QLocale.Chinese, QLocale.Taiwan)
    ENGLISH = QLocale(QLocale.English)
    AUTO = QLocale()
    
class LogLevel(Enum):
    """ Log level enumeration class """
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    
    def __contains__(self, item):
        if item in [self.DEBUG, self.INFO]:
            return True
        else:
            return False

class LogLevelSerializer:
    """ log Level serializer """

    def serialize(self, level):
        return level.value if level in LogLevel else LogLevel.INFO.value

    def deserialize(self, value):
        return LogLevel(value) if value in LogLevel else LogLevel.INFO

class LanguageSerializer(ConfigSerializer):
    """ Language serializer """

    @staticmethod
    def serialize(language):
        return Language.value.name() if language != Language.AUTO else "Auto"

    @staticmethod
    def deserialize(value: str):
        return Language(QLocale(value)) if value != "Auto" else Language.AUTO

class Config(QConfig):
    """ Config of application """

    # main window
    logLevel = OptionsConfigItem("Setting", "log_level","INFO", OptionsValidator(["DEBUG", "INFO"]))
    language = OptionsConfigItem("Setting", "language", "zh_CN", OptionsValidator(["en_US", "zh_CN", "zh_TW", "Auto"]))


# 创建配置实例并使用配置文件来初始化它
cfg = Config()
qconfig.load(":/config/config.json", cfg)
