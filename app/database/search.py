from .db_config import Config
from app.utils.crypto import CryptoHasher
from app.utils.logger.logger import logger
import uuid
import sqlite3


class Searchdb:
    def __init__(self) -> None:
        self.connect = sqlite3.connect(Config.PATHS.get("video_db"))
        self.INIT_SEARCH_DB_SQL = Config.load(
            Config.PATHS.get("init_search_history_db_sql")
        )
        self.trigger = Config.load(Config.PATHS.get("search_trigger"))
        self.init()

    def create_trigger(self) -> None:
        try:
            self.connect.execute(self.trigger)
            self.connect.commit()
        except sqlite3.Error as e:
            logger.error(f"create trigger fail: {e}")
            self.connect.rollback()
    
    def init(self) -> None:
        try:
            self.connect.execute(self.INIT_SEARCH_DB_SQL)
            self.connect.commit()
        except sqlite3.Error as e:
            logger.error(f"init search db fail: {e}")
            self.connect.rollback()

    def destroy(self, db_name: str) -> None:
        try:
            self.connect.execute(f"DROP TABLE IF EXISTS {db_name};")
            self.connect.commit()
        except sqlite3.Error as e:
            logger.error(f"destroy db fail: {e}")
            self.connect.rollback()

    def search(self, keyword: str) -> list:
        try:
            result = self.connect.execute(Config.SEARCH_ALL, keyword).fetchall()
            return result
        except sqlite3.Error as e:
            logger.error(f"search fail: {e}")
            return []
        finally:
            self.connect.close()
