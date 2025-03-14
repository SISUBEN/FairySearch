from app.__init__ import *
from app.libs.login import LoginWindow
from app.assets.resourceManager import ResourceManager
from app.libs.expection import UnsupportedLanguageError
from app.libs.dialog import Dialog
from app.utils.logger.logger import logger
from app.i18n import _
rm = ResourceManager()
dialog = Dialog()
if __name__ == "__main__":
    try:
        console = Console()
        console.print(Rule(_("初始化")))
        
        app = QApplication([])
        tanslator = rm.getTranslator()
        app.installTranslator(tanslator)
        app.setWindowIcon(QIcon(":/icons/icons/icon.ico"))
        
        loginWindow = LoginWindow()
        loginWindow.show()
        
        app.exec()
    except KeyboardInterrupt:
        logger.error(_(f"The program was interrupted by the user"))
    except UnsupportedLanguageError:
        pass
    finally:
        app.shutdown()