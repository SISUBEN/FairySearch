import sqlite3
from .db_config import Config
from app.utils.crypto import CryptoHasher
from app.modules.logger.logger import logger
import uuid

cryptor = CryptoHasher()
config = Config()
class Database:
    def __init__(self):
        with open(config.USER_SQL, "r") as file:
            config.USER_SQL = file.read()
        with open(config.VIDEO_SQL, "r") as file:
            config.VIDEO_SQL = file.read()
        
    class Userdb:
        def __init__(self) -> None:
            self.user_connect = sqlite3.connect(config.USER_DB)
            self.user_cur = self.user_connect.cursor()
            self.init_userdb()

        def init_userdb(self) -> None:
            try:
                self.user_connect.execute(config.USER_SQL)
                self.user_connect.commit()
            except sqlite3.Error as e:
                logger.debug(f"init user db fail: {e}")
                self.user_connect.rollback()
        def user_add(self, username: str, password: str) -> None:
            try:
                self.user_connect.execute(config.USER_ADD, (username, password))
                self.user_connect.commit()
            except sqlite3.Error as e:
                logger.debug(f"add user fail: {e}")
                self.user_connect.rollback()

        def t_user_add(self, username: str, password: str) -> str:
            """Add user to database with token

            Args:
                username (str): username
                password (str): password must be plain text
            """
            try:
                encrypted = cryptor.sha256(password)
                token = self.generate_token(username, encrypted)
                self.user_connect.execute(config.T_USER_ADD, (username, encrypted, token))
                self.user_connect.commit()
                return token
            except sqlite3.Error as e:
                logger.debug(f"add user token fail: {e}")
                self.user_connect.rollback()
            except Exception as e:
                logger.debug(f"create token fail: {e}")
            
        def verify_token(self, token: str) -> bool:
            """Verify token

            Args:
                token (str): token

            Returns:
                bool: is True if token is valid
            """
            try:
                return self.user_connect.execute(config.T_USER_QUERY, (token,)).fetchone() is not None
            except sqlite3.Error as e:
                logger.debug(f"verify token error: {e}")

        def get_token(self, username: str) -> str:
            """Get token by username

            Args:
                username (str): username

            Returns:
                str: token
                
            Exception:
                sqlite3.Error: if error occurs
            """
            try:
                 return self.user_connect.execute(config.T_USER_QUERY, (username,)).fetchone()[0][0]
            except sqlite3.Error as e:
                logger.debug(f"get token error: {e}")
        
        
        def generate_token(self, username: str, password: str) -> str:
            """Generate token for user

            Args:
                username (str): username plain text
                password (str): password cipher text

            Raises:
                Exception: if user not exists

            Returns:
                str[64]: token (a sha256 hash)
            """
            token = {
                "username": username,
                "pasword": password, 
            }
            token = str(token)
            return cryptor.sha256(token)
                
        
        def user_exists(self, username: str) -> bool:
            """Check if user exists

            Args:
                username (str): username

            Returns:
                bool: is Ture if user exists
                
            Exception:
                sqlite3.Error: if error occurs
            """
            try: 
                return (
                    self.user_connect.execute(config.USER_QUERY, (username,)).fetchone()
                    is not None
                ) # if query result is not None, return True, else return result
            except sqlite3.Error as e:
                logger.debug(f"An error occurred when querying user exists: {e}")
        
        def query_username(self, token: str) -> list:
            """query username by token

            Args:
                token (str): login token

            Returns:
                str: username
            """
            try:
                return self.user_connect.execute(config.T_USERNAME_QUERY, (token,)).fetchall()[0][0]
            except sqlite3.Error as e:
                logger.debug(f"query username error: {e}")

        def destroy_db(self, db_name: str) -> None:
            try:
                self.user_connect.execute(f"DROP TABLE IF EXISTS {db_name};")
                self.user_connect.commit()
            except sqlite3.Error as e:
                logger.debug(f"destroy db fail: {e}")
                
        def query_user_password(self, username: str) -> str:
            """Query user password by username

            Args:
                username (str): username

            Returns:
                str: user password
            """
            logger.debug(f"self.user_connect.execute(config.USER_QUERY_PWD, (username,)).fetchall() = {self.user_connect.execute(config.USER_QUERY_PWD, (username,)).fetchall()}")
            try:
                return self.user_connect.execute(config.USER_QUERY_PWD, (username,)).fetchall()[0][0]
            except sqlite3.Error as e:
                logger.debug(f"query user password error: {e}")
                
        def query_user_uid(self, username: str) -> int:
            """Query user uid by username

            Args:
                username (str): username

            Returns:
                int : user uid
                
            Exception:
                sqlite3.Error: if query fail
            """
            try:
                return self.user_connect.execute(config.USER_QUERY_UID, (username,)).fetchall()[0][0]
            except sqlite3.Error as e:
                logger.debug(f"query user uid error: {e}")

        def query_uid(self, token: str) -> int:
            """Query user uid by token

            Args:
                token (str): login token

            Returns:
                int: user uid
                
            Exception:
                sqlite3.Error: if query fail
            """
            try:
                return self.user_connect.execute(config.T_USER_QUERY_UID, (token,)).fetchall()[0][0]
            except sqlite3.Error as e:
                logger.debug(f"query uid error: {e}")
        
        def verify_user(self, password: str, username: str) -> bool:
            """Verfy user password

            Args:
                password (str): user password (encrypted)
                username (str): username

            Returns:
                bool: True if password is correct, False otherwise
            """
            logger.debug(f"pwd: {password}, username: {username}")
            logger.debug(f"Is user exists? => {self.user_exists(username)}")
            logger.debug(f"self.user_connect.execute(config.USER_QUERY_PWD, (username,)).fetchall() = {self.user_connect.execute(config.USER_QUERY_PWD, (username,)).fetchall()}")
            return self.query_user_password(username) == password

        def __del__(self) -> None:
            self.user_connect.close()
    
    class SearchHistorydb:
        def __init__(self) -> None:
            self.search_connect = sqlite3.connect(config.USER_DB)
            self.init_searchdb()

        def __del__(self):
            self.search_connect.close()

        def init_searchdb(self) -> None:
            try:
                self.search_connect.execute(config.INIT_SH_DB)
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


    class Videodb:
        def __init__(self) -> None:
            self.video_connect = sqlite3.connect(config.VIDEO_DB)
            self.video_cur = self.video_connect.cursor()
            self.init_videodb()

        def init_videodb(self) -> None:
            try:
                self.video_connect.execute(config.VIDEO_SQL)
                self.video_connect.commit()
            except sqlite3.Error as e:
                logger.debug(f"init videodb fail: {e}")
                self.video_connect.rollback()

        def video_add(
            self,
            video_title: str,
            video_time_sec: float,
            video_type: str,
            video_tags: list,
            video_desc: str,
            video_cover_path: str = config.DEFAULT_COVER,
        ):
            """add video to database

            Args:
                video_title (str): video title
                video_time_sec (float): video time
                video_type (str): video type
                video_tags (list): video tags
                video_desc (str): video description
                video_cover_path (str, optional): path of video cover (qrc path). Defaults to config.DEFAULT_COVER.
            
            Exception:
                sqlite3.Error: if add fail
            """
            if self.video_query(video_title):
                return
            elif len(video_title) > config.TITLE_MAX_LEN:
                return
            tags = ",".join(video_tags)
            types = ",".join(video_type)
            try:
                self.video_connect.execute(
                    config.VIDEO_ADD,
                    (
                        video_title,
                        video_cover_path,
                        video_time_sec,
                        types,
                        tags,
                        video_desc,
                    ),
                )
                self.video_connect.commit()
            except sqlite3.Error as e:
                logger.debug(f"add video error: {e}")
                self.video_connect.rollback()

        def count_videos(self) -> int:
            try:
                return int(self.video_connect.execute(config.VIDEO_COUNT).fetchone()[0])
            except sqlite3.Error as e:
                logger.debug(f"count videos error: {e}")
            finally:
                self.video_connect.close()

        def video_query(self, video_id: int) -> tuple:
            try:
                return self.video_connect.execute(config.VIDEO_QUERY, (video_id,)).fetchall()[0]
            except sqlite3.Error as e:
                logger.debug(f"video query error: {e}")

        def query_title_by_vid(self, vid: int) -> str:
            try:
                logger.debug(f"title: {self.video_connect.execute(config.VIDEO_QUERY_TITLE, (vid,)).fetchall()[0][0]}\nvid: {vid}")
                return self.video_connect.execute(config.VIDEO_QUERY_TITLE, (vid,)).fetchall()
            
            except sqlite3.Error as e:
                logger.debug(f"query title by vid error: {e}")
            
        def query_desc_by_vid(self, vid: int) -> str:
            try:
                return self.video_connect.execute(config.VIDEO_QUERY_DESC, (vid,)).fetchall()
            except sqlite3.Error as e:
                logger.debug(f"query desc by vid error: {e}")
            
                
        def query_videos_by_page(self, page: int, page_size: int) -> tuple:
            try:
                return self.video_connect.execute(
                    config.VIDEO_QUERY_BY_PAGE, (page, page_size)
                ).fetchall()[0]
            except sqlite3.Error as e:
                logger.debug(f"query videos by page error: {e}")

        def query_videos_all(self) -> list:
            """Query all videos
            
            Return:
                list: all videos e.g. [(1, 'title', 'path', 100, 'type1,type2', 'tag1,tag2', 'desc')]
            """
            try:
                return self.video_connect.execute(config.VIDEO_QUERY_ALL).fetchall()
            except sqlite3.Error as e:
                logger.debug(f"query videos all error: {e}")
        
        def destroy_db(self, db_name: str) -> None:
            self.video_connect.execute(f"DROP TABLE IF EXISTS {db_name};")
            # self.video_connect.execute(f"ALTER TABLE {db_name} AUTO_INCREMENT=1")
            self.video_connect.commit()

        def __del__(self) -> None:
            self.video_connect.close()

    userdb = Userdb()
    videodb = Videodb()
    searchHisdb = SearchHistorydb()
