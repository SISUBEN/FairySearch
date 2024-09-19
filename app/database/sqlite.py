import sqlite3
from config import *

class Database:
    class SearchHistorydb():
        def __init__(self) -> None:
            self.search_connect = sqlite3.connect(SH_DB)
            self.search_cur = self.search_connect.cursor()
            self.init_searchdb()
        
        def __del__(self):
            self.search_connect.close()
        
        def init_searchdb(self) -> None:
            self.search_connect.execute(
                INIT_SH_DB
            )
            self.search_connect.commit()
            
        def search_history_add(self, uid: int, username: str, title: str, time: str) -> None:
            self.search_connect.execute(
                SH_ADD,
                (uid, username, title, time)
            )
            self.search_connect.commit()
        
        def query_search_history(self, username: str, latest: int) -> list:
            if latest == 0:                
                return self.search_connect.execute(
                        QUERY_SH,
                        (username,)
                ).fetchall()
            elif latest < 0 or isinstance(latest, int):
                return TypeError
            else:
                return self.search_connect.execute(
                        FILTE_SH,
                        (username, latest)
                ).fetchall()
            
        def destroy_db(self, db_name: str) -> None:
            self.search_connect.execute(DESTROY_SH, (db_name,))
            self.search_connect.commit()
            
    class Userdb():
        def __init__(self) -> None:
            self.user_connect = sqlite3.connect(USER_DB)
            self.user_cur = self.user_connect.cursor()
            self.init_userdb()
    
        def init_userdb(self) -> None:
            self.user_connect.execute(
                INIT_USER_DB
            )
            self.user_connect.commit()
        
        def user_add(self, username: str, password: str) -> None: # 添加用户
            self.user_connect.execute(
                "INSERT INTO users VALUES (?, ?);",
                (username, password)
            )
            self.user_connect.commit()
    
        def user_exists(self, username: str) -> bool | tuple: # 用户是否存在
            return self.user_connect.execute(
            "SELECT * FROM users WHERE username=?;", (username,)
            ).fetchone() is not None # 如果查询结果为空，则返回None，否则返回查询结果
    
        def destroy_db(self, db_name: str) -> None:
            self.user_connect.execute("DROP TABLE IF EXISTS ?;", (db_name,))
            self.user_connect.commit()
        
        def query_user_password(self, username: str) -> list:
            return self.user_connect.execute(
                    "SELECT password FROM users WHERE username=?;",
                    (username,)
            ).fetchall()
            
        def query_user_uid(self, username: str) -> list:
            return self.user_connect.execute(
                    "SELECT uid FROM users WHERE username=?;",
                    (username,)
            ).fetchall()
            
        def __del__(self) -> None:
            self.user_connect.close()

    class Videodb():
        def __init__(self) -> None:
            self.video_connect = sqlite3.connect(VIDEO_DB)
            self.video_cur = self.video_connect.cursor()
            self.init_videodb()
    
        def init_videodb(self) -> None: # 创建视频数据库
            self.video_connect.execute(
                """CREATE TABLE IF NOT EXISTS videos (
                    video_id INTEGER PRIMARY KEY,
                    video_title VARCHAR(20),
                    video_cover_path TEXT,
                    video_time_sec FLAOT,
                    video_type VARCHAR(20),
                    video_tags VARCHAR(20),
                    video_desc TEXT
                );"""
            )
            self.video_connect.commit()
        
        def video_add(
            self, 
            video_title: str,
            video_time_sec: float,
            video_type: str,
            video_tags: list,
            video_desc: str,
            video_cover_path: str = DEFAULT_COVER
        ):
            if self.video_query(video_title):
                return
            elif len(video_title) > TITLE_MAX_LEN or \
            len(video_type) > TITLE_MAX_LEN or \
            len(video_tags) > TAG_MAX_LEN or \
            len(video_desc) > DESC_MAX_LEN:
                
                return
            tags = ",".join(video_tags)
            types = ",".join(video_type)
            self.video_connect.execute(
                "INSERT INTO videos VALUES (?, ?, ?, ?, ?);",
                (video_title, video_cover_path, video_time_sec, tags, types)
            )
            self.video_connect.commit()
        
        def video_query(self, video_id: int) -> list:
            return self.video_connect.execute(
                    "SELECT * FROM videos WHERE video_id=?;",
                    (video_id,)
            ).fetchall()
    
        def __del__(self) -> None:
            self.video_connect.close()

    userdb = Userdb()
    videodb = Videodb()