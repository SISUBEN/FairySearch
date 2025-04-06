# db addr
from PySide6.QtCore import QFile, QTextStream
from dataclasses import dataclass
from app.utils.logger.logger import logger
import app.assets.resources_rc
import os

logger.debug(f"Current file dir: {os.getcwd()}")


@dataclass
class Config:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # locate database path automatically
    # Database sql path
    PATHS = {
        "video_db": os.path.join(current_dir, "videos.db"),
        "user_db": os.path.join(current_dir, "users.db"),
        "import_data_sql": ":/data_sql/sql/import_data.sql",
        "video_activity_data_sql": ":/table_sql/sql/video_activity_data.sql",
        "init_video_db_sql": ":/table_sql/sql/init_video_db.sql",
        "init_user_db_sql": ":/table_sql/sql/init_user_db.sql",
        "init_search_history_db_sql": ":/table_sql/sql/init_search_history_db.sql",
        "create_trigger_sql": ":/table_sql/sql/create_triggers.sql"
    }
    @staticmethod
    def load(resource_path: str) -> str:
        file = QFile(resource_path)
        if not file.open(QFile.ReadOnly | QFile.Text):
            logger.error(f"Cannot open resource file: {resource_path}")
            raise FileNotFoundError(f"Cannot open resource file: {resource_path}")
        stream = QTextStream(file)
        content = stream.readAll()
        file.close()
        return content

    # default
    DEFAULT_COVER = ":/covers/covers/default.png"
    # SQL
    RESET_ID = "alter table ? AUTO_INCREMENT=1;"
    # search history
    QUERY_SH = "SELECT title FROM search_history WHERE userid=?;"
    COUNT_SH = "SELECT COUNT(*) FROM search_history WHERE userid=?;"
    FILTE_SH = "SELECT title, timestamp, duration FROM search_history WHERE userid=? ORDER BY timestamp DESC LIMIT ? OFFSET ?;"
    FILTE_SH_ALL = "SELECT title, timestamp, duration, uuid, vid FROM search_history WHERE userid=? ORDER BY timestamp"
    SH_ADD = "INSERT INTO search_history (uuid, vid, userid ,title, timestamp, duration) VALUES (?, ?, ?, ?, ?, ?);"
    # user
    USER_ADD = "INSERT INTO users (username, password, token) VALUES (?, ?, ?);"
    USER_QUERY_EXISTS = "SELECT * FROM users WHERE username=?;"
    USER_QUERY = "SELECT * FROM users WHERE token=?;"
    USERNAME_QUERY = "SELECT username FROM users WHERE token=?;"
    USER_QUERY_PWD = "SELECT password FROM users WHERE token=?;"
    USER_QUERY_PWD_BY_USRNAME = "SELECT password FROM users WHERE username=?;"
    USER_QUERY_UID = "SELECT uid FROM users WHERE token=?;"
    USER_QUERY_TOKEN = "SELECT token FROM users WHERE username=?;"
    DESTROY_TABLE = "DROP TABLE IF EXISTS ?;"
    # video
    VIDEO_ADD = "INSERT INTO videos (video_title, video_cover_path, video_time_sec, video_type, video_tags, video_desc) VALUES (?, ?, ?, ?, ?, ?);"
    VIDEO_QUERY = "SELECT * FROM videos WHERE video_id=?;"
    VIDEO_QUERY_BY_PAGE = "SELECT * FROM videos ORDER BY video_id DESC LIMIT ?,?;"
    VIDEO_QUERY_ALL = "SELECT * FROM videos;"
    VIDEO_COUNT = "SELECT COUNT(*) FROM videos"
    VIDEO_QUERY_TITLE = "SELECT video_title FROM videos WHERE video_id = ?;"
    VIDEO_QUERY_DESC = "SELECT video_desc FROM videos WHERE video_id = ?;"
    VIDEO_QUERY_TAG = "SELECT video_id FROM videos WHERE video_tag = ?;"
    # search
    SEARCH_ALL = "SELECT TITLE, SUMMARY, URL FROM videos_fts WHERE videos_fts MATCH jieba_query(?);"
