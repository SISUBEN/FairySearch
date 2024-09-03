import sqlite3
from .config import Config

class Database:
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
                    video_time_sec INTEGER,
                    video_type VARCHAR(5)
                );"""
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