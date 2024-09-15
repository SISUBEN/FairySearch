import sqlite
# sh_db = sqlite.Database.SearchHistorydb()
video_db = sqlite.Database.Videodb()
# user_db = sqlite.Database.Userdb()
video_db.init_videodb()
video_db.