import sqlite3
from .db_config import Config
from app.utils.crypto import CryptoHasher
from app.utils.logger.logger import logger
import uuid


class SearchHistorydb:
    def __init__(self) -> None:
        self.cryptor = CryptoHasher()
        self.search_connect = sqlite3.connect(Config.PATHS["user_db"])
        self.INIT_SH_DB_SQL = Config.load(Config.PATHS["init_search_history_db_sql"])
        self.init_searchdb()

    def __del__(self):
        self.search_connect.close()