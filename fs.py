# Copyright 2025 SISUBENY

# Permission is hereby granted, free of charge, 
# to any person obtaining a copy of this software and associated documentation files (the “Software”), 
# to deal in the Software without restriction, including without limitation the rights to use, 
# copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies 
# or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from app.__init__ import Console, Rule, QApplication, QIcon
from app.libs.login import LoginWindow
from app.assets.resource_manager import ResourceManager
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
        rm = ResourceManager(app)
        rm.setTranslation()
        app.setWindowIcon(QIcon(":/icons/icons/icon.ico"))

        loginWindow = LoginWindow(app)
        loginWindow.show()

        app.exec()
    except KeyboardInterrupt:
        logger.error(_(f"The program was interrupted by the user"))
    except UnsupportedLanguageError:
        pass
    finally:
        app.shutdown()
