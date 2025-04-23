from .db_config import Config
from app.utils.crypto import CryptoHasher
from app.utils.logger.logger import logger
from app.assets.resource_manager import ResourceManager
import uuid
import sqlite3
import traceback
import os


class Searchdb:
    def __init__(self) -> None:
        self.res_mgr = ResourceManager()
        self.connect = sqlite3.connect(Config.PATHS.get("video_db"))
        self.init_search_db = Config.load(Config.PATHS.get("init_fts_sql"))
        self.triggers = Config.load(Config.PATHS.get("triggers_sql"))
        # # detect is video and video_fts exists
        # result = self.connect.execute(
        #     "SELECT name FROM sqlite_master WHERE type='table' AND name='videos' OR name='videos_fts';"
        # ).fetchone()
        # if result is None:
        self.init()

    def init(self) -> None:
        try:
            cursor = self.connect.cursor()
            if self.is_exist("videos_fts") is False:
                cursor.executescript(self.init_search_db)
            cursor.executescript(self.triggers)
            # using 3rd party SQLite3 fts5 tokenizer (simple) to search Chinese word
            # Github: https://github.com/wangfenjin/simple/issues
            # simple licensed under MIT license
            self.ext_path = self.res_mgr.get3rdPartyLibs("libsimple", "simple.dll")
            self.connect.enable_load_extension(True)
            self.connect.load_extension(self.ext_path)
            self.connect.commit()
        except sqlite3.Error as e:
            logger.error(f"init search db fail: {traceback.format_exc()}")
            self.connect.rollback()

    def is_exist(self, db_name: str) -> bool:
        """
        Checks if a database with the given name exists.

        Args:
            db_name (str): The name of the database to check.

        Returns:
            bool: True if the database exists, False otherwise.
        """
        cursor = self.connect.cursor()
        result = cursor.execute(Config.DB_IS_EXISTS, (db_name,)).fetchone()
        return result is not None

    def destroy(self, db_name: str) -> None:
        try:
            self.connect.execute(f"DROP TABLE IF EXISTS {db_name};")
            self.connect.commit()
        except sqlite3.Error as e:
            logger.error(f"destroy db fail: {traceback.format_exc()}")
            self.connect.rollback()

    def search(self, keyword: str) -> list:
        """
        Search the database for entries matching the given keyword.

        Executes a SQL query using the predefined SIMPLE_SEARCH configuration.
        Handles database errors gracefully, returns an empty list on failure.
        Switches to default search mode if engine initialization fails.

        Args:
            keyword (str): The search term to query in the database.

        Returns:
            list: A list of matching records. Returns empty list if error occurs.

        Note:
            Always closes the database connection after execution.
        """
        try:
            path = self.res_mgr.get3rdPartyDir("libsimple")
            os.chdir(path)
            # result = self.connect.execute(Config.SEARCH_ALL, (keyword,))
            result = self.connect.execute(Config.SIMPLE_SEARCH, (keyword,))
            return result.fetchall()
        except sqlite3.Error as e:
            logger.error(f"search fail: {traceback.format_exc()}")
            return []
        except sqlite3.OperationalError:
            logger.error("Fail to init search engine, change to default search mode")
            result = self.connect.execute(Config.SIMPLE_SEARCH, (keyword,))
            return result.fetchall()

    def __del__(self):
        self.connect.close()
        del self.connect
