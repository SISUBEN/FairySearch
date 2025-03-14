from dataclasses import dataclass, field
from typing import List
from PySide6.QtCore import QTranslator

import locale
import os

from app.utils.logger.logger import logger
from app.libs.expection import UnsupportedLanguageError

@dataclass
class ResourceManager:
    current_dir: str = os.path.dirname(os.path.abspath(__file__))
    covers_dir: str = os.path.join(current_dir, "covers")
    videos_dir: str = os.path.join(current_dir, "videos")
    locale_lang: str = locale.getdefaultlocale()[0]
    # PEP 557: Using default factory functions to create new instances of mutable types as default values for fields
    support_lang: List[str] = field(default_factory=lambda: ["en", "zh_CN", "zh_TW"])

    def getVideoPath(self, vid: int, file_type: str = "mp4", isEscape: bool = True) -> str:
        """get video file path

        Args:
            vid (int): video id
            file_type (str, optional): type of file. Defaults to "mp4".

        Returns:
            _type_: video file path
        """
        if os.path.exists(p := os.path.join(self.videos_dir, f"{vid}.{file_type}")):
            return p if isEscape else p.replace("\\", "/")
        else:
            return None

    def getCoverPath(self, vid: int, file_type: str = "png", isEscape: bool = True) -> str:
        """get cover file path
        
        Args:
            vid (int): video id
            file_type (str, optional): type of file. Defaults to "png".

        Returns:
            _type_: cover file path
        """
        if os.path.exists(p := os.path.join(self.covers_dir, f"{vid}.{file_type}")):
            return p if isEscape else p.replace("\\", "/")
        else:
            return None

    def getI18nDirectory(self) -> None:
        """
        Constructs the path to the 'i18n' directory within the current directory.

        Returns:
            None
        """
        return os.path.join(self.current_dir, "i18n")
    
    def getTranslationPath(self, trans_file: str = "") -> str:
        """Get translation file path

        Args:
            trans_file (str, optional): translate file. Defaults to "" and auto detect.

        Returns:
            str: translate file path
        """        
        return os.path.join(self.getI18nDirectory(), trans_file if trans_file else self.locale_lang + ".qm")
    
    def getTranslator(self, trans_file: str = "") -> QTranslator:
        """install translation

        Args:
            app (QApplication): Pyside6 application
            trans_file (str, optional): tanslate file. Defaults to "" and auto detect.  
            
        Raises:
            UnsupportedLanguageError: if language is not supported  
            
        Returns:
            QTranslator: translator
            
        """
        if self.locale_lang not in self.support_lang: raise UnsupportedLanguageError(self.locale_lang)
        translator = QTranslator()
        file = trans_file if trans_file else self.locale_lang + ".qm"
        logger.info(f"Loading translation file: {file}")
        logger.debug(f"load {'successful' if translator.load(file, self.getI18nDirectory()) else 'failed'}")
        if translator.load(file, self.getI18nDirectory()):
            return translator