from qfluentwidgets import (
    QConfig,
    ConfigItem,
    BoolValidator,
    ConfigSerializer,
    qconfig,
    OptionsConfigItem,
    OptionsValidator,
    exceptionHandler,
    Path
)
from PySide6.QtCore import QLocale, Qt, QObject, QFile, QTextStream
from app.utils.logger.logger import logger
from enum import Enum
import json
import logging

class Language(Enum):
    """Language enumeration class"""

    SIMP_CHINESE = QLocale(QLocale.Chinese, QLocale.China)
    TRA_CHINESE = QLocale(QLocale.Chinese, QLocale.Taiwan)
    ENGLISH = QLocale(QLocale.English)
    AUTO = QLocale()


class LogLevel(Enum):
    """Log level enumeration class"""

    DEBUG = logging.DEBUG
    INFO = logging.INFO

    def __contains__(self, item):
        if item in [self.DEBUG, self.INFO]:
            return True
        else:
            return False


class LogLevelSerializer:
    """log Level serializer"""

    def serialize(self, level):
        return level.value if level in LogLevel else LogLevel.INFO.value

    def deserialize(self, value):
        return LogLevel(value) if value in LogLevel else LogLevel.INFO


class LanguageSerializer(ConfigSerializer):
    """Language serializer"""

    @staticmethod
    def serialize(language):
        return language.value.name() if language != Language.AUTO else "Auto"

    @staticmethod
    def deserialize(value: str):
        return Language(QLocale(value)) if value != "Auto" else Language.AUTO

class Config(QConfig):
    """Config of application"""

    # main window
    logLevel = OptionsConfigItem(
        "Setting", "logLevel", "INFO", OptionsValidator(["DEBUG", "INFO"])
    )
    language = OptionsConfigItem(
        "Setting",
        "Language",
        "zh_CN",
        OptionsValidator(["en_US", "zh_CN", "zh_TW", "Auto"]),
    )


cfg = Config()
qconfig.load("config/config.json", cfg)
