from app.__init__ import *
from app.libs.login import LoginWindow
import gettext
import threading

# thread local storage
thread = threading.local()


def set_lang(language: str):
    thread.trans = gettext.translation('app', localedir='locales', languages=[language])

def translate(text: str):
    return thread.trans.gettext(text)

if __name__ == "__main__":
    try:
        set_lang("zh-CN")
        console = Console()
        console.print(Rule("Initializing"))
        app = QApplication([])
        app.setWindowIcon(QIcon(":/icons/icons/icon.ico"))
        loginWindow = LoginWindow()
        loginWindow.show()
        app.exec()
    except Exception as err:
        logger.critical(f"An error occurred while the program was running: {err}")
        app.shutdown()
    except KeyboardInterrupt:
        logger.error("The program was interrupted by the user")
        app.shutdown()
