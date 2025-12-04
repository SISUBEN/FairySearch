# Author: SISUBENY
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

from app import Console, Rule, QApplication, QIcon
from app.assets.resource_manager import ResourceManager
from app.database.db_config import DatabaseQueryManager as QueryMgr
from app.libs.login import LoginWindow
from app.libs.exception import UnsupportedLanguageError
from app.libs.dialog import Dialog
from app.utils.logger.logger import logger
from app.i18n import _

import pretty_errors

if __name__ == "__main__":
    try:
        console = Console()
        console.print(Rule("Initializing"))

        app = QApplication([])
        QueryMgr.load_queries()
        logger.debug("Database queries loaded")
        rm = ResourceManager(app)
        rm.setTranslation()
        app.setWindowIcon(QIcon(":/icons/icons/icon.ico"))

        try:
            dialog = Dialog()
            loginWindow = LoginWindow(app)
        except Exception as e:
            logger.error(f"Error initializing UI components: {e}")
            raise
        loginWindow.show()
        app.exec()
    except KeyboardInterrupt:
        logger.error(f"The program was interrupted by the user")
    finally:
        app.shutdown()
