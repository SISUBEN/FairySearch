# db addr
import os
from app.modules.logger.logger import logger
from dataclasses import dataclass
from typing import ClassVar

logger.debug(f"Current file dir: {os.getcwd()}")


@dataclass
class Config:
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # locate database path automatically
    USER_SQL: str
    VIDEO_SQL: str
    SEARCH_HISTORY_SQL: str
    
    # Database sql path
    VIDEO_DB: str = os.path.join(current_dir, "videos.db")
    USER_DB: str = os.path.join(current_dir, "users.db")
    VIDEO_SQL_PATH: str = os.path.join(current_dir, "videos_db.sql")
    USER_SQL_PATH: str = os.path.join(current_dir, "user_db.sql")
    SEARCH_HISTORY_SQL_PATH: str = os.path.join(current_dir, "search_history.sql")
    
    # default
    DEFAULT_COVER: str = os.path.join(current_dir, "covers", "default.png")
    
    # SQL
    RESET_ID = "alter table ? AUTO_INCREMENT=1;"
    # search history
    INIT_SH_DB = """CREATE TABLE IF NOT EXISTS search_history (
                        uuid CHAR(33) PRIMARY KEY,
                        vid INTEGER NOT NULL,
                        userid INTEGER NOT NULL,
                        title VARCHAR(32) NOT NULL,
                        timestamp INTEGER NOT NULL,
                        duration INTEGER NOT NULL,
                        FOREIGN KEY (userid) REFERENCES users(uid)
                    );"""
    QUERY_SH = "SELECT title FROM search_history WHERE userid=?;"
    COUNT_SH = "SELECT COUNT(*) FROM search_history WHERE userid=?;"
    FILTE_SH = "SELECT title, timestamp, duration FROM search_history WHERE userid=? ORDER BY timestamp DESC LIMIT ? OFFSET ?;"
    FILTE_SH_ALL = "SELECT title, timestamp, duration, uuid, vid FROM search_history WHERE userid=? ORDER BY timestamp"
    SH_ADD = "INSERT INTO search_history (uuid, vid, userid ,title, timestamp, duration) VALUES (?, ?, ?, ?, ?, ?);"
    # user
    INIT_USER_DB = """CREATE TABLE IF NOT EXISTS users (
                        uid INTEGER PRIMARY KEY AUTOINCREMENT,
                        username VARCHAR(32) NOT NULL,
                        password VARCHAR(32) NOT NULL,
                        token VARCHAR(32) NOT NULL
                    );"""
    USER_ADD = "INSERT INTO users (username, password) VALUES (?, ?);"
    USER_QUERY = "SELECT * FROM users WHERE username=?;"
    USER_QUERY_PWD = "SELECT password FROM users WHERE username=?;"
    USER_QUERY_UID = "SELECT uid FROM users WHERE username=?;"
    # T_ for token-base auth method
    T_USER_ADD = "INSERT INTO users (username, password, token) VALUES (?, ?, ?);"
    T_USER_QUERY = "SELECT * FROM users WHERE token=?;"
    T_USERNAME_QUERY = "SELECT username FROM users WHERE token=?;"
    T_USER_QUERY_PWD = "SELECT password FROM users WHERE token=?;"
    T_USER_QUERY_UID = "SELECT uid FROM users WHERE token=?;"
    USER_QUERY_TOKEN = "SELECT token FROM users WHERE username=?;"
    DESTROY_TABLE = "DROP TABLE IF EXISTS ?;"
    # video
    INIT_VIDEO_DB = """CREATE TABLE IF NOT EXISTS videos (
                        video_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        video_title VARCHAR(50),
                        video_cover_path TEXT,
                        video_time_sec FLOAT,
                        video_type TEXT,
                        video_tags TEXT,
                        video_desc TEXT
                    );"""
    VIDEO_ADD = "INSERT INTO videos (video_title, video_cover_path, video_time_sec, video_type, video_tags, video_desc) VALUES (?, ?, ?, ?, ?, ?);"
    VIDEO_QUERY = "SELECT * FROM videos WHERE video_id=?;"
    VIDEO_QUERY_BY_PAGE = """
        SELECT * FROM videos ORDER BY video_id DESC LIMIT ?,?;
    """
    VIDEO_QUERY_ALL = "SELECT * FROM videos;"
    VIDEO_COUNT = "SELECT COUNT(*) FROM videos"
    VIDEO_QUERY_TITLE = "SELECT video_title FROM videos WHERE video_id = ?;"
    VIDEO_QUERY_DESC = "SELECT video_desc FROM videos WHERE video_id = ?;"


try:
    # logger.debug(
    #     f"is path exists: {os.path.exists(Config.USER_SQL_PATH), os.path.exists(Config.VIDEO_SQL_PATH), os.path.exists(Config.SEARCH_HISTORY_SQL_PATH)}"
    # )
    with open(Config.USER_SQL_PATH, "r") as file:
        Config.USER_SQL = file.read()
    with open(Config.VIDEO_SQL_PATH, "r") as file:
        Config.VIDEO_SQL = file.read()
    with open(Config.SEARCH_HISTORY_SQL_PATH, "r") as file:
        Config.SEARCH_HISTORY_SQL = file.read()
        
    # logger.debug(
    #     f"user sql length: {len(Config.USER_SQL)}\nvideo sql length: {len(Config.VIDEO_SQL)}\n search history sql length: {len(Config.SEARCH_HISTORY_SQL)}"
    # )
except FileNotFoundError:
    logger.critical("database file not found")
    exit()
