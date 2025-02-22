from dataclasses import dataclass
from PySide6.QtCore import QTranslator
from PySide6.QtWidgets import QApplication
import locale
import os

from app.modules.logger.logger import logger


@dataclass
class ResourceManager:
    current_dir: str = os.path.dirname(os.path.abspath(__file__))
    covers_dir: str = os.path.join(current_dir, "covers")
    videos_dir: str = os.path.join(current_dir, "videos")

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

    def installTranslation(self, app: QApplication, trans_file: str = "", directory: str = "") -> None:
        """install translation

        Args:
            trans_file (str): translation file name
            directory (str, optional):  i18n directory. "" to auto detect. Defaults to "".
        """
        translator = QTranslator()
        file = trans_file.lower() if trans_file else locale.getdefaultlocale()[0] + ".qm"
        directory = directory if directory else os.path.join(self.current_dir, "i18n")
        file = "en.qm"
        logger.info(f"Loading translation file: {file}")
        logger.debug(f"loda {translator.load(file, directory)}")
        if translator.load(file, directory):
            app.installTranslator(translator)
