# Author: SISUBENY <https://github.com/SISUBEN>
# Version: 0.0.1
# Date: 2025-03-23
# License: GPL-3.0-or-later

# Copyright (c) 2025-2026 SISUBENY

# This file is part of FairySearch.
# FairySearch is free software: you can redistribute it and/or modify it under the terms of the 
# GNU General Public License as published by the Free Software Foundation, 
# either version 3 of the License, or (at your option) any later version.
# FairySearch is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with FairySearch. 
# If not, see <https://www.gnu.org/licenses/>.

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
