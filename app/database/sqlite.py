import sqlite3
from .config import Config

class Database:

    class SearchHistorydb():
        def __init__(self) -> None:
            self.search_connect = sqlite3.connect(Config.search_history_db)
            self.search_cur = self.search_connect.cursor()
            self.init_searchdb()
        
        def __del__(self):
            self.search_connect.close()
        
        def init_searchdb(self) -> None:
            self.search_connect.execute(
                """CREATE TABLE IF NOT EXISTS search_history (
                    uid INTEGER ,
                    username VARCHAR(32) NOT NULL,
                    title VARCHAR(32) NOT NULL,
                    time DATETIME NOT NULL,
                );"""
            )
            self.search_connect.commit()
            
        def search_history_add(self, uid: int, username: str, title: str, time: str) -> None:
            self.search_connect.execute(
                "INSERT INTO search_history VALUES (?, ?, ?, ?);",
                (uid, username, title, time)
            )
            self.search_connect.commit()
        
        def query_search_history(self, username: str, latest: int) -> list:
            if latest == 0:                
                return self.search_connect.execute(
                        "SELECT title FROM search_history WHERE username=?;",
                        (username,)
                ).fetchall()
            elif latest < 0 or isinstance(latest, int):
                return TypeError
            else:
                return self.search_connect.execute(
                        "SELECT title FROM search_history WHERE username=? ORDER BY time DESC LIMIT ?;",
                        (username, latest)
                ).fetchall()
            
        def destroy_db(self, db_name: str) -> None:
            self.search_connect.execute("DROP TABLE IF EXISTS ?;", (db_name,))
            self.search_connect.commit()
            
    class Userdb():
        def __init__(self) -> None:
            self.user_connect = sqlite3.connect(Config.videos_db)
            self.user_cur = self.user_connect.cursor()
            self.init_userdb()
    
        def init_userdb(self) -> None:
            self.user_connect.execute(
                """CREATE TABLE IF NOT EXISTS users (
                    uid INTEGER PRIMARY KEY AUTOINCREMENT,
                    username VARCHAR(32) NOT NULL,
                    password VARCHAR(32) NOT NULL
                );"""
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
            self.video_connect = sqlite3.connect(Config.videos_db)
            self.video_cur = self.video_connect.cursor()
            self.init_videodb()
    
        def init_videodb(self) -> None: # 创建视频数据库
            self.video_connect.execute(
                """CREATE TABLE IF NOT EXISTS videos (
                    video_id INTEGER PRIMARY KEY,
                    video_name VARCHAR(20),
                    video_cover_path TEXT,
                    video_time_sec DOUBLE,
                    video_type VARCHAR(5),
                    video_tags VARCHAR(20)
                );"""
            )
            self.video_connect.commit()
        
        def video_add(
            self, 
            video_name: str,
            video_time_sec: float,
            video_type: str,
            video_tags: list,
            video_cover_path: str = Config.DEFAULT_COVER
        ):
            tags = ",".join(video_tags)
            self.video_connect.execute(
                "INSERT INTO videos VALUES (?, ?, ?, ?, ?);",
                (video_name, video_cover_path, video_time_sec, tags, video_type)
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