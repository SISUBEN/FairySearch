from .db_config import Config
from app.utils.crypto import CryptoHasher
from app.utils.logger.logger import logger
from app.database.base import Database
from app.database.db_config import DatabaseQueryManager as QueryMgr
import uuid
import sqlite3

class SearchHistorydb(Database):
    def __init__(self) -> None:
        self.cryptor = CryptoHasher()
        self.connect = sqlite3.connect(Config.get_path("user_db"))
        self.INIT_SH_DB_SQL = Config.load(Config.get_path("init_search_history_db_sql"))
        self.init()

    def init(self) -> None:
        try:
            self.connect.execute(self.INIT_SH_DB_SQL)
            self.connect.commit()
        except sqlite3.Error as e:
            logger.error(f"init search db fail: {e}")

    def get_total_history(self, username: str) -> int:
        """
        Retrieves the total number of search history entries for a given user.
        
        Args:
            username (str): The username for which the search history count is retrieved.
        Returns:
            int: The total number of search history entries for the specified user.
        Raises:
            sqlite3.Error: If an error occurs during the database query.
        """
        try:
            return self.connect.execute(QueryMgr.get_query("search_history.count_sh"), (username,)).fetchone()[
                0
            ]
        except sqlite3.Error as e:
            logger.error(f"get total historys error: {e}")

    def generate_uuid(self) -> str:
        return uuid.uuid4().hex

    def insert(
        self,
        uuid: str,
        vid: int,
        userid: int,
        title: str,
        timestamp: str,
        duration: str,
    ) -> None:
        """
        Inserts a new search history record into the database.

        Args:
            uuid (str): A unique identifier for the search history entry.
            vid (int): The video ID associated with the search.
            userid (int): The user ID who performed the search.
            title (str): The title of the search or video.
            timestamp (str): The timestamp of when the search was performed.
            duration (str): The duration of the search or video.

        Returns:
            None

        Raises:
            sqlite3.Error: If an error occurs during the database operation.
        """
        try:
            self.connect.execute(
                QueryMgr.get_query("search_history.add_sh"), (uuid, vid, userid, title, timestamp, duration)
            )
            self.connect.commit()
        except sqlite3.Error as e:
            logger.error(f"add search history fail: {e}")
            self.connect.rollback()

    def query(self, userid: int, page_size: int, page_num: int) -> list:
        """
        Query the search history for a specific user with pagination.
        
        Args:
            userid (int): The ID of the user whose search history is being queried.
            page_size (int): The number of records to retrieve per page.
            page_num (int): The page number to retrieve (1-based index).
            
        Returns:
            list: A list of search history records for the specified user and page.
            
        Raises:
            sqlite3.Error: If an error occurs during the database query.
        """
        offset = (page_num - 1) * page_size
        from app.database.db_config import DatabaseQueryManager as QueryMgr
        try:
            return self.connect.execute(
                QueryMgr.get_query("search_history.query_sh"), (userid, offset, page_size)
            ).fetchall()
        except sqlite3.Error as e:
            logger.error(f"query search history error: {e}")

    def query_all(self, userid: int) -> list:
        """
        Retrieve all search history records for a given user.
        Args:
            userid (int): The ID of the user whose search history is to be retrieved.
        Returns:
            list: A list of all search history records associated with the given user.
        Raises:
            sqlite3.Error: If an error occurs during the database query.
        """
        
        try:
            return self.connect.execute(
                QueryMgr.get_query("search_history.filte_sh_all"), (userid,)
            ).fetchall()
        except sqlite3.Error as e:
            logger.error(f"query search history error: {e}")

    def destroy(self, db_name: str) -> None:
        try:
            self.connect.execute(f"DROP TABLE IF EXISTS {db_name};")
            self.connect.commit()
        except sqlite3.Error as e:
            logger.error(f"destroy db fail: {e}")