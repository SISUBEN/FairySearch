import sqlite3
from .db_config import Config
from app.utils.crypto import CryptoHasher
from app.utils.logger.logger import logger
cryptor = CryptoHasher()
config = Config

class Videodb:
        def __init__(self) -> None:
            self.video_connect = sqlite3.connect(config.PATHS["video_db"])
            self.video_cur = self.video_connect.cursor()
            self.init_videodb()

        def init_videodb(self) -> None:
            try:
                self.video_connect.execute(config.INIT_VIDEO_DB)
                self.video_connect.commit()
            except sqlite3.Error as e:
                logger.debug(f"init videodb fail: {e}")
                self.video_connect.rollback()

        def video_add(
            self,
            video_title: str,
            video_time_sec: float,
            video_type: str,
            video_tags: list,
            video_desc: str,
            video_cover_path: str = config.DEFAULT_COVER,
        ):
            """add video to database

            Args:
                video_title (str): video title
                video_time_sec (float): video time
                video_type (str): video type
                video_tags (list): video tags
                video_desc (str): video description
                video_cover_path (str, optional): path of video cover (qrc path). Defaults to config.DEFAULT_COVER.
            
            Exception:
                sqlite3.Error: if add fail
            """
            if self.video_query(video_title):
                return
            tags = ",".join(video_tags)
            types = ",".join(video_type)
            try:
                self.video_connect.execute(
                    config.VIDEO_ADD,
                    (
                        video_title,
                        video_cover_path,
                        video_time_sec,
                        types,
                        tags,
                        video_desc,
                    ),
                )
                self.video_connect.commit()
            except sqlite3.Error as e:
                logger.debug(f"add video error: {e}")
                self.video_connect.rollback()

        def count_videos(self) -> int:
            try:
                return int(self.video_connect.execute(config.VIDEO_COUNT).fetchone()[0])
            except sqlite3.Error as e:
                logger.debug(f"count videos error: {e}")
            finally:
                self.video_connect.close()

        def video_query(self, video_id: int) -> tuple:
            try:
                return self.video_connect.execute(config.VIDEO_QUERY, (video_id,)).fetchall()[0]
            except sqlite3.Error as e:
                logger.debug(f"video query error: {e}")

        def query_title_by_vid(self, vid: int) -> str:
            try:
                logger.debug(f"title: {self.video_connect.execute(config.VIDEO_QUERY_TITLE, (vid,)).fetchall()[0][0]}\nvid: {vid}")
                return self.video_connect.execute(config.VIDEO_QUERY_TITLE, (vid,)).fetchall()
            
            except sqlite3.Error as e:
                logger.debug(f"query title by vid error: {e}")
            
        def query_desc_by_vid(self, vid: int) -> str:
            try:
                return self.video_connect.execute(config.VIDEO_QUERY_DESC, (vid,)).fetchall()
            except sqlite3.Error as e:
                logger.debug(f"query desc by vid error: {e}")
            
                
        def query_videos_by_page(self, page: int, page_size: int) -> tuple:
            try:
                return self.video_connect.execute(
                    config.VIDEO_QUERY_BY_PAGE, (page, page_size)
                ).fetchall()[0]
            except sqlite3.Error as e:
                logger.debug(f"query videos by page error: {e}")

        def query_videos_all(self) -> list:
            """Query all videos
            
            Return:
                list: all videos e.g. [(1, 'title', 'path', 100, 'type1,type2', 'tag1,tag2', 'desc')]
            """
            try:
                return self.video_connect.execute(config.VIDEO_QUERY_ALL).fetchall()
            except sqlite3.Error as e:
                logger.debug(f"query videos all error: {e}")
        
        def destroy_db(self, db_name: str) -> None:
            self.video_connect.execute(f"DROP TABLE IF EXISTS {db_name};")
            # self.video_connect.execute(f"ALTER TABLE {db_name} AUTO_INCREMENT=1")
            self.video_connect.commit()

        def __del__(self) -> None:
            self.video_connect.close()