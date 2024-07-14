import sqlite3
from config import Config

class DatabaseTool:
    config = Config()
    def __init__(self) -> None:
        self.user_connect = sqlite3.connect(Config.videos_db)
        self.video_connect = sqlite3.connect(Config.videos_db)
        self.user_cur = self.user_connect.cursor()
        self.video_cur = self.video_connect.cursor()
        
    def userdb_build(self) -> None: # 创建用户数据库
        self.user_connect.execute(
            """CREATE TABLE IF NOT EXISTS users(
                username VARCHAR(32) PRIMARY KEY,
                password VARCHAR(32)
            )"""
        )
        self.user_connect.commit()
        
    def user_add(self, username: str, password: str) -> None: # 添加用户
        self.user_connect.execute(
            "INSERT INTO users VALUES (?, ?)",
            (username, password)
        )
        self.user_connect.commit()
    
    def user_exists(self, username: str) -> bool | tuple: # 用户是否存在
        return self.user_connect.execute(
           "SELECT * FROM users WHERE username=?", (username,)
        ).fetchone() is not None # 如果查询结果为空，则返回None，否则返回查询结果
    
    def destroy_db(self, db_name: str) -> None:
        self.user_connect.execute("DROP TABLE IF EXISTS ?", (db_name,))
        self.user_connect.commit()
    
    def query_user_password(self, username: str) -> list:
        return self.user_connect.execute(
                "SELECT password FROM users WHERE username=?",
                (username,)
        ).fetchall()
    
    def videodb_build(self) -> None: # 创建视频数据库
        self.video_connect.execute(
            """CREATE TABLE IF NOT EXISTS videos(
                video_id INTEGER PRIMARY KEY,
                video_name VARCHAR(20),
                video_cover_path TEXT,
                video_time_sec INTEGER(10),
                video_type VARCHAR(5),
            )"""
        )
        self.video_connect.commit()
    
    def video_query(self, video_id: int) -> list:
        # 迭代器
        return self.video_connect.execute(
                "SELECT * FROM videos WHERE video_id=?",
                (video_id,)
        ).fetchall()
    
    def __del__(self) -> None:
        self.user_connect.close()
        
# TODO: 创建视频数据库
# TODO: 创建视频表