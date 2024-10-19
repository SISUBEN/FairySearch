# db addr
# 请使用启动脚本启动main.py
# 否则路径可能会出错
# 或者请使用绝对路径
VIDEO_DB: str = "./app/database/videos.db"
USER_DB: str = "./app/database/users.db"
SH_DB: str = "./app/database/search_history.db"
# default
DEFAULT_COVER = "./app/database/covers/default.png"
# max value
TYPE_MAX_LEN = 50
TITLE_MAX_LEN = 50
DESC_MAX_LEN = 100
TAG_MAX_LEN = 50
# SQL
RESET_ID = "alter table ? AUTO_INCREMENT=1;"
# search history
INIT_SH_DB = """CREATE TABLE IF NOT EXISTS search_history (
                    uid INTEGER ,
                    username VARCHAR(32) NOT NULL,
                    title VARCHAR(32) NOT NULL,
                    time DATETIME NOT NULL,
                );"""
QUERY_SH = "SELECT title FROM search_history WHERE username=?;"
FILTE_SH = (
    "SELECT title FROM search_history WHERE username=? ORDER BY time DESC LIMIT ?;"
)
SH_ADD = "INSERT INTO search_history (uid, username ,title, time) VALUES (?, ?, ?, ?);"
# user
INIT_USER_DB = """CREATE TABLE IF NOT EXISTS users (
                    uid INTEGER PRIMARY KEY AUTOINCREMENT,
                    username VARCHAR(32) NOT NULL,
                    password VARCHAR(32) NOT NULL
                );"""
USER_ADD = "INSERT INTO users (username, password) VALUES (?, ?);"
USER_QUERY = "SELECT * FROM users WHERE username=?;"
USER_QUERY_PWD = "SELECT password FROM users WHERE username=?;"
USER_QUERY_UID = "SELECT uid FROM users WHERE username=?;"
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

VIDEO_COUNT = "SELECT COUNT(*) FROM videos"