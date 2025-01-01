from app.database.users import Userdb
from app.database.search_history import SearchHistorydb
from app.database.videos import Videodb

class Database:
    userdb = Userdb()
    videodb = Videodb()
    searchHisdb = SearchHistorydb()