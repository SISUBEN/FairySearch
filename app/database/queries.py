import sqlite3
from .config import *

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
            
        def get_total_historys(self, username: str) -> int:
            return self.search_connect.execute(
                COUNT_SH, (username,)
            ).fetchone()[0]
        
        def search_history_add(self, uid: int, username: str, title: str, time: str) -> None:
            self.search_connect.execute(
                SH_ADD,
                (uid, username, title, time)
            )
            self.search_connect.commit()
        
        def query_search_history(self, username: str, page_size: int, page_num: int) -> list:
            offset = (page_num - 1) * page_size
            return self.search_connect.execute(
                FILTE_SH, (username, offset, page_size)
            ).fetchall()
            
            
        def destroy_db(self, db_name: str) -> None:
            self.search_connect.execute(f"DROP TABLE IF EXISTS {db_name};")
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
                USER_ADD,
                (username, password)
            )
            self.user_connect.commit()
    
        def user_exists(self, username: str) -> bool | tuple: # 用户是否存在
            return self.user_connect.execute(
            USER_QUERY, (username,)
            ).fetchone() is not None # 如果查询结果为空，则返回None，否则返回查询结果
    
        def destroy_db(self, db_name: str) -> None:
            self.user_connect.execute(f"DROP TABLE IF EXISTS {db_name};")
            self.user_connect.commit()
        
        def query_user_password(self, username: str) -> list:
            return self.user_connect.execute(
                    USER_QUERY_PWD,
                    (username,)
            ).fetchall()
            
        def query_user_uid(self, username: str) -> list:
            return self.user_connect.execute(
                    USER_QUERY_UID,
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
                INIT_VIDEO_DB
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
            elif len(video_title) > TITLE_MAX_LEN:    
                return
            tags = ",".join(video_tags)
            types = ",".join(video_type)
            self.video_connect.execute(
                VIDEO_ADD,
                (video_title, video_cover_path, video_time_sec, types, tags, video_desc)
            )
            self.video_connect.commit()
        
        def count_videos(self) -> int:
            return int(self.video_connect.execute(
                VIDEO_COUNT
            ).fetchone()[0])
        
        def video_query(self, video_id: int) -> list:
            return self.video_connect.execute(
                    VIDEO_QUERY,
                    (video_id,)
            ).fetchall()
            
        def query_videos_by_page(self, page: int, page_size: int) -> list:
            return self.video_connect.execute(
                VIDEO_QUERY_BY_PAGE,
                (page, page_size)
            ).fetchall()
    
        def destroy_db(self, db_name: str) -> None:
            self.video_connect.execute(f"DROP TABLE IF EXISTS {db_name};")
            # self.video_connect.execute(f"ALTER TABLE {db_name} AUTO_INCREMENT=1")
            self.video_connect.commit()
            
        def __del__(self) -> None:
            self.video_connect.close()

    userdb = Userdb()
    videodb = Videodb()
    searchHisdb = SearchHistorydb()