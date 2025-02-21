from app.__init__ import *
from app.libs.login import LoginWindow
from app.i18n import _

if __name__ == "__main__":
    try:
        
        # locale_lang = locale.getdefaultlocale()[0]
        locale_lang = 'en_US'
        console = Console()
        console.print(Rule(_("初始化")))
        app = QApplication([])
        app.setWindowIcon(QIcon(":/icons/icons/icon.ico"))
        loginWindow = LoginWindow()
        loginWindow.show()
        app.exec()
    except Exception as err:
        logger.critical(_(f"An error occurred while the program was running: {err}"))
        app.shutdown()
    except KeyboardInterrupt:
        logger.error(_(f"The program was interrupted by the user"))
        app.shutdown()
