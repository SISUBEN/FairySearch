import sqlite3
from .db_config import Config
from app.utils.crypto import CryptoHasher
from app.modules.logger.logger import logger
import uuid
cryptor = CryptoHasher()
config = Config

class SearchHistorydb:
        def __init__(self) -> None:
            self.search_connect = sqlite3.connect(config.USER_DB)
            self.init_searchdb()

        def __del__(self):
            self.search_connect.close()

        def init_searchdb(self) -> None:
            try:
                self.search_connect.execute(config.SEARCH_HISTORY_SQL)
                self.search_connect.commit()
            except sqlite3.Error as e:
                logger.debug(f"init search db fail: {e}")

        def get_total_historys(self, username: str) -> int:
            try:
                return self.search_connect.execute(config.COUNT_SH, (username,)).fetchone()[0]
            except sqlite3.Error as e:
                logger.debug(f"get total historys error: {e}")

        def generate_uuid(self) -> str:
            return uuid.uuid4().hex

        def search_history_add(
            self, uuid: str, vid: int, userid: int, title: str, timestamp: str, duration: str
        ) -> None:
            try:
                self.search_connect.execute(
                    config.SH_ADD, (uuid, vid, userid, title, timestamp, duration)
                )
                self.search_connect.commit()
            except sqlite3.Error as e:
                logger.debug(f"add search history fail: {e}")
                self.search_connect.rollback()

        def query_search_history(
            self, userid: int, page_size: int, page_num: int
        ) -> list:
            offset = (page_num - 1) * page_size
            try:
                return self.search_connect.execute(
                    config.FILTE_SH, (userid, offset, page_size)
                ).fetchall()
            except sqlite3.Error as e:
                logger.debug(f"query search history error: {e}")
            
        def query_search_history_all(self, userid: int) -> list:
            try:
                return self.search_connect.execute(config.FILTE_SH_ALL, (userid,)).fetchall()
            except sqlite3.Error as e:
                logger.debug(f"query search history error: {e}")

        def destroy_db(self, db_name: str) -> None:
            try:
                self.search_connect.execute(f"DROP TABLE IF EXISTS {db_name};")
                self.search_connect.commit()
            except sqlite3.Error as e:
                logger.debug(f"destroy db fail: {e}")