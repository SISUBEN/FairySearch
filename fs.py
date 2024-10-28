from app.__init__ import *
from app.libs.login import LoginWindow
from PySide6.QtCore import QtMsgType, qInstallMessageHandler
import os

if __name__ == "__main__":
    try:
        console = Console()
        console.print(Rule("Initializing"))
        app = QApplication([])
        app.setWindowIcon(QIcon(":/icons/icons/icon.ico"))
        loginWindow = LoginWindow()
        loginWindow.show()
        app.exec()
    except Exception as err:
        logger.critical(
            f"An error occurred while the program was running: {err}")  
        app.shutdown()
    except KeyboardInterrupt:
        logger.error("The program was interrupted by the user")
        app.shutdown()