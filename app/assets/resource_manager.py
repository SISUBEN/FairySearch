from typing import List
from PySide6.QtCore import QFile, QTextStream, QTranslator
from PySide6.QtWidgets import QApplication
from app.utils.logger.logger import logger
from app.libs.expection import UnsupportedLanguageError, ResourceNotFoundError
from app.assets import resources_rc
import locale
import os


class ResourceManager:
    def __init__(self, application: QApplication = None):
        self.app = application
        self.current_dir: str = os.path.dirname(os.path.abspath(__file__))
        logger.debug(self.current_dir)
        # TODO: change to QRC path mode
        self.covers_dir: str = os.path.join(self.current_dir, "covers")
        self.videos_dir: str = os.path.join(self.current_dir, "videos")
        self.i18n_dir: str = os.path.join(self.current_dir, "i18n")

        self.locale_lang: str = locale.getdefaultlocale()[0]
        self.support_lang: List[str] = ["en_US", "zh_CN", "zh_TW"]

    def getVideoPath(
        self, vid: int, file_type: str = "mp4", isEscape: bool = True
    ) -> str | None:
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

    def getCoverPath(
        self, vid: int, file_type: str = "png", isEscape: bool = True
    ) -> str | None:
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
        return os.path.join(
            self.getI18nDirectory(),
            trans_file if trans_file else self.locale_lang + ".qm",
        )

    def get3rdPartyLibs(self, name: str, libs: str = "") -> str:
        path = os.path.join(self.current_dir, "3rdParty", name, libs)
        # path = "c:\\Users\\32426\\Desktop\\toolbox\\.code\\py\\FairySearch\\app\\assets\\3rdParty\\libsimple"
        logger.debug(path)
        if os.path.exists(path) is True:
            return path
        else:
            raise ResourceNotFoundError
    def get3rdPartyDir(self, name: str) -> str:
        path = os.path.join(self.current_dir, "3rdParty", name)
        logger.debug(path)
        if os.path.exists(path) is True:
            return path
        else:
            raise ResourceNotFoundError

    def getTranslator(self, lang: str = "Auto") -> QTranslator:
        """get translator

        Args:
            app (QApplication): Pyside6 application
            trans (str, optional): tanslate lang. Defaults to "Auto" and auto detect.

        Raises:
            UnsupportedLanguageError: if language is not supported

        Returns:
            QTranslator: translator

        """
        lang = self.locale_lang if lang == "Auto" else lang
        if lang not in self.support_lang:
            raise UnsupportedLanguageError(self.locale_lang)
        translator = QTranslator()
        file = lang if lang != "Auto" else self.locale_lang + ".qm"
        logger.info(f"Loading translation file: {file}")
        if translator.load(file, self.getI18nDirectory()):
            return translator

    def setTranslation(self, lang: str = "Auto") -> None:
        """set translation

        Args:
            app (QApplication): Pyside6 application
            trans (str, optional): tanslate lang. Defaults to "Auto" and auto detect.

        Raises:
            UnsupportedLanguageError: if language is not supported

        Returns:
            None
        """
        self.translator = self.getTranslator(lang)
        self.app.installTranslator(self.translator)

    @staticmethod
    def load(resource_path: str) -> str:
        """load qrc file

        Args:
            file (str): qrc file path

        Returns:
            str: file content
        """
        file = QFile(resource_path)
        if not file.open(QFile.ReadOnly | QFile.Text):
            logger.error(f"Cannot open resource file: {resource_path}")
            raise FileNotFoundError(f"Cannot open resource file: {resource_path}")
        stream = QTextStream(file)
        content = stream.readAll()
        file.close()
        return content

    # def uninstallTranslation(self, lang: str) -> None:
    #     self.app.removeTranslator(self.translator)
