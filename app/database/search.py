from .db_config import Config
from app.utils.crypto import CryptoHasher
from app.utils.logger.logger import logger
from app.assets.resource_manager import ResourceManager
import uuid
import sqlite3



class Searchdb:
    def __init__(self) -> None:
        self.res_mgr = ResourceManager()
        self.connect = sqlite3.connect(Config.PATHS.get("video_db"))
        self.INIT_SEARCH_DB_SQL = Config.load(
            Config.PATHS.get("init_search_history_db_sql")
        )
        self.ad_trigger = Config.load(Config.PATHS.get("after_del_trigger_sql"))
        self.au_trigger = Config.load(Config.PATHS.get("after_upd_trigger_sql"))
        self.ai_trigger = Config.load(Config.PATHS.get("after_ins_trigger_sql"))
        self.init()
    
    def init(self) -> None:
        try:
            import pdb
            # pdb.set_trace()
            self.connect.execute(self.INIT_SEARCH_DB_SQL)
            # using 3rd party SQLite3 fts5 tokenizer (simple) to search Chinese word 
            # Github: https://github.com/wangfenjin/simple/issues
            # simple licensed under MIT license
            self.ext_path = self.res_mgr.get3rdPartyLibs("libsimple", "simple.dll")
            # logger.debug(self.ext_path)
            self.connect.enable_load_extension(True)
            # self.connect.pe
            self.connect.load_extension(self.ext_path)
            cursor = self.connect.cursor()
            cursor.execute(self.ad_trigger)
            cursor.execute(self.au_trigger)
            cursor.execute(self.ai_trigger)
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
            path = self.res_mgr.get3rdPartyDir("libsimple")
            import os
            os.chdir(path=path)
            result = self.connect.execute(Config.SEARCH_ALL, (keyword, ))
            return result.fetchall()
        except sqlite3.Error as e:
            logger.error(f"search fail: {e}")
            return []
        finally:
            self.connect.close()
