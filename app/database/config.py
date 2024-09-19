
# db addr
VIDEO_DB: str = "./app/database/vidoes.db"
USER_DB: str = "./app/database/users.db"
SH_DB: str = "./app/database/search_history.db"
# default
DEFAULT_COVER = "./covers/default.png"
# max value
TYPE_MAX_LEN = 50
TITLE_MAX_LEN = 50
DESC_MAX_LEN = 100
TAG_MAX_LEN = 50
# SQL
INIT_SH_DB = """CREATE TABLE IF NOT EXISTS search_history (
                    uid INTEGER ,
                    username VARCHAR(32) NOT NULL,
                    title VARCHAR(32) NOT NULL,
                    time DATETIME NOT NULL,
                );"""
QUERY_SH = "SELECT title FROM search_history WHERE username=?;"
FILTE_SH = "SELECT title FROM search_history WHERE username=? ORDER BY time DESC LIMIT ?;"
SH_ADD = "INSERT INTO search_history VALUES (?, ?, ?, ?);"
DESTROY_SH = "DELETE FROM search_history WHERE username=?;"
    
INIT_USER_DB = """CREATE TABLE IF NOT EXISTS users (
                    uid INTEGER PRIMARY KEY AUTOINCREMENT,
                    username VARCHAR(32) NOT NULL,
                    password VARCHAR(32) NOT NULL
                );"""