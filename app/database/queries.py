import sqlite3
from .db_config import *
from app.utils.crypto import CryptoHasher
import time
import uuid

cryptor = CryptoHasher()

class Database:
    class SearchHistorydb:
        def __init__(self) -> None:
            self.search_connect = sqlite3.connect(SH_DB)
            self.search_cur = self.search_connect.cursor()
            self.init_searchdb()

        def __del__(self):
            self.search_connect.close()

        def init_searchdb(self) -> None:
            self.search_connect.execute(INIT_SH_DB)
            self.search_connect.commit()

        def get_total_historys(self, username: str) -> int:
            return self.search_connect.execute(COUNT_SH, (username,)).fetchone()[0]

        def generate_uuid(self) -> str:
            return uuid.uuid4().hex

        def search_history_add(
            self, uuid: str, userid: int, title: str, timestamp: str, duration: str
        ) -> None:

            self.search_connect.execute(
                SH_ADD, (uuid, userid, title, timestamp, duration)
            )
            self.search_connect.commit()

        def query_search_history(
            self, userid: int, page_size: int, page_num: int
        ) -> list:
            offset = (page_num - 1) * page_size
            return self.search_connect.execute(
                FILTE_SH, (userid, offset, page_size)
            ).fetchall()
            
        def query_search_history_all(self, userid: int) -> list:
            return self.search_connect.execute(
                FILTE_SH_ALL, (userid,)
            ).fetchall()

        def destroy_db(self, db_name: str) -> None:
            self.search_connect.execute(f"DROP TABLE IF EXISTS {db_name};")
            self.search_connect.commit()

    class Userdb:
        def __init__(self) -> None:
            import os
            import sys
            from app.modules.logger.logger import logger
            logger.debug(f"is userdb exists: {os.path.exists(USER_DB)}\n\tcurrent work dir: {os.path.dirname(os.path.abspath(__file__))}")
            self.user_connect = sqlite3.connect(USER_DB)
            self.user_cur = self.user_connect.cursor()
            self.init_userdb()

        def init_userdb(self) -> None:
            self.user_connect.execute(INIT_USER_DB)
            self.user_connect.commit()

        def user_add(self, username: str, password: str) -> None:
            self.user_connect.execute(USER_ADD, (username, password))
            self.user_connect.commit()

        def t_user_add(self, username: str, password: str) -> str:
            """Add user to database with token

            Args:
                username (str): username
                password (str): password must be plain text
            """
            encrypted = cryptor.sha256(password)
            token = self.generate_token(username, encrypted)
            self.user_connect.execute(T_USER_ADD, (username, encrypted, token))
            self.user_connect.commit()
            return token
            
        def verify_token(self, token: str) -> bool:
            """Verify token

            Args:
                token (str): token

            Returns:
                bool: is True if token is valid
            """
            return self.user_connect.execute(T_USER_QUERY, (token,)).fetchone() is not None

        def get_token(self, username: str) -> str:
            return self.user_connect.execute(T_USER_QUERY, (username,)).fetchone()[0]
        
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
            """
            return (
                self.user_connect.execute(USER_QUERY, (username,)).fetchone()
                is not None
            ) # if query result is not None, return True, else return result
            

        def destroy_db(self, db_name: str) -> None:
            self.user_connect.execute(f"DROP TABLE IF EXISTS {db_name};")
            self.user_connect.commit()

        def query_user_password(self, username: str) -> list:
            """Query user password by username

            Args:
                username (str): username

            Returns:
                list: result example: [('password',)]
            """
            return self.user_connect.execute(USER_QUERY_PWD, (username,)).fetchall()

        def query_user_uid(self, username: str) -> list:
            """Query user uid by username

            Args:
                username (str): username

            Returns:
                list: result example: [('uid',)]
            """
            return self.user_connect.execute(USER_QUERY_UID, (username,)).fetchall()
        
        def verify_user(self, password: str, username: str) -> bool:
            """Verfy user password

            Args:
                password (str): user password (encrypted)
                username (str): username

            Returns:
                bool: True if password is correct, False otherwise
            """
            if self.user_exists(username):
                return self.query_user_password(username)[0][0] == password
            else:
                return False

        def __del__(self) -> None:
            self.user_connect.close()

    class Videodb:
        def __init__(self) -> None:
            self.video_connect = sqlite3.connect(VIDEO_DB)
            self.video_cur = self.video_connect.cursor()
            self.init_videodb()

        def init_videodb(self) -> None:
            self.video_connect.execute(INIT_VIDEO_DB)
            self.video_connect.commit()

        def video_add(
            self,
            video_title: str,
            video_time_sec: float,
            video_type: str,
            video_tags: list,
            video_desc: str,
            video_cover_path: str = DEFAULT_COVER,
        ):
            """add video to database

            Args:
                video_title (str): video title
                video_time_sec (float): video time
                video_type (str): video type
                video_tags (list): video tags
                video_desc (str): video description
                video_cover_path (str, optional): path of video cover (qrc path). Defaults to DEFAULT_COVER.
            """
            if self.video_query(video_title):
                return
            elif len(video_title) > TITLE_MAX_LEN:
                return
            tags = ",".join(video_tags)
            types = ",".join(video_type)
            self.video_connect.execute(
                VIDEO_ADD,
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

        def count_videos(self) -> int:
            return int(self.video_connect.execute(VIDEO_COUNT).fetchone()[0])

        def video_query(self, video_id: int) -> list:
            return self.video_connect.execute(VIDEO_QUERY, (video_id,)).fetchall()

        def query_videos_by_page(self, page: int, page_size: int) -> list:
            return self.video_connect.execute(
                VIDEO_QUERY_BY_PAGE, (page, page_size)
            ).fetchall()

        def destroy_db(self, db_name: str) -> None:
            self.video_connect.execute(f"DROP TABLE IF EXISTS {db_name};")
            # self.video_connect.execute(f"ALTER TABLE {db_name} AUTO_INCREMENT=1")
            self.video_connect.commit()

        def __del__(self) -> None:
            self.video_connect.close()

    userdb = Userdb()
    videodb = Videodb()
    searchHisdb = SearchHistorydb()
