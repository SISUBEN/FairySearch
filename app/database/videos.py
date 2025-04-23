import sqlite3
from .db_config import Config
from app.utils.crypto import CryptoHasher
from app.utils.logger.logger import logger


class Videodb:
    def __init__(self) -> None:
        self.cryptor = CryptoHasher()
        self.connect = sqlite3.connect(Config.PATHS.get("video_db"))
        self.INIT_VIDEO_DB_SQL = Config.load(Config.PATHS.get("init_video_db_sql"))
        self.init()

    def init(self) -> None:
        try:
            self.connect.execute(self.INIT_VIDEO_DB_SQL)
            self.connect.commit()
        except sqlite3.Error as e:
            logger.error(f"init videodb fail: {e}")
            self.connect.rollback()
    
    def insert(
        self,
        video_title: str,
        video_time_sec: float,
        video_type: str,
        video_tags: list,
        video_desc: str,
        video_cover_path: str = Config.DEFAULT_COVER,
    ):
        """insert video to database

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
        if self.is_video_exist(video_title):
            return
        tags = ",".join(video_tags)
        types = ",".join(video_type)
        try:
            self.connect.execute(
                Config.VIDEO_ADD,
                (
                    video_title,
                    video_cover_path,
                    video_time_sec,
                    types,
                    tags,
                    video_desc,
                ),
            )
            self.connect.commit()
        except sqlite3.Error as e:
            logger.debug(f"add video error: {e}")
            self.connect.rollback()

    def count_videos(self) -> int:
        try:
            return int(self.connect.execute(Config.VIDEO_COUNT).fetchone()[0])
        except sqlite3.Error as e:
            logger.debug(f"count videos error: {e}")
        finally:
            self.connect.close()
        
    def is_video_exist(self, video_title: str) -> bool:
        try:
            return bool(
                self.connect.execute(
                    Config.VIDEO_QUERY_TITLE, (video_title,)
                ).fetchone()
            )
        except sqlite3.Error as e:
            logger.debug(f"is video exist error: {e}")

    def get(self, video_id: int) -> tuple:
        """
        Get target video record from database
        Args:
            video_id (int): The ID of the video to get.
        Returns:
            tuple: A tuple containing the video record data.
        Raises:
            sqlite3.Error: If an error occurs during the database query, it is logged.
        """

        try:
            logger.debug(video_id)
            result = self.connect.execute(
                Config.VIDEO_QUERY, (video_id,)
            ).fetchall()[0]
            logger.debug(result)
            return result
        except sqlite3.Error as e:
            logger.debug(f"video query error: {e}")

    def query_title_by_vid(self, vid: int) -> str:
        """
        Queries the database for the title of a video based on its video ID (vid).
        Args:
            vid (int): The unique identifier of the video.
        Returns:
            str: The title of the video if the query is successful.
        Raises:
            sqlite3.Error: If an error occurs during the database query.
        """
        try:
            logger.debug(
                f"title: {self.connect.execute(Config.VIDEO_QUERY_TITLE, (vid,)).fetchall()[0][0]}\nvid: {vid}"
            )
            return self.connect.execute(
                Config.VIDEO_QUERY_TITLE, (vid,)
            ).fetchall()

        except sqlite3.Error as e:
            logger.debug(f"query title by vid error: {e}")

    def query_desc_by_vid(self, vid: int) -> str:
        """
        Retrieves the description of a video from the database based on its video ID.
        Args:
            vid (int): The ID of the video whose description is to be retrieved.
        Returns:
            str: The description of the video.
        Raises:
            sqlite3.Error: If a database error occurs during the query execution.
        """
        try:
            return self.connect.execute(
                Config.VIDEO_QUERY_DESC, (vid,)
            ).fetchall()[0][0]
        except sqlite3.Error as e:
            logger.debug(f"query desc by vid error: {e}")

    def query_videos_by_page(self, page: int, page_size: int) -> tuple:
        """
        Queries videos from the database based on the specified page and page size.
        Args:
            page (int): The page number to retrieve videos from.
            page_size (int): The number of videos to retrieve per page.
        Returns:
            tuple: A tuple containing the queried video records.
        Raises:
            sqlite3.Error: If an error occurs during the database query.
        """

        try:
            return self.connect.execute(
                Config.VIDEO_QUERY_BY_PAGE, (page, page_size)
            ).fetchall()[0]
        except sqlite3.Error as e:
            logger.debug(f"query videos by page error: {e}")

    def query_videos_all(self) -> list:
        """Query all videos

        Return:
            list: all videos e.g. [(1, 'title', 'path', 100, 'type1,type2', 'tag1,tag2', 'desc')]

        Raises:
            sqlite3.Error: if query fail
        """
        try:
            return self.connect.execute(Config.VIDEO_QUERY_ALL).fetchall()
        except sqlite3.Error as e:
            logger.debug(f"query videos all error: {e}")

    def query(self, tag: str) -> list:
        """Query videos by tag

        Args:
            type (str): video tag

        Return:
            list: videos id

        Raises:
            sqlite3.Error: if query fail
        """
        try:
            return self.connect.execute(Config.VIDEO_QUERY_TAG, (tag,)).fetchall()
        except sqlite3.Error as e:
            logger.debug(f"query videos by type error: {e}")

    def destroy(self, db_name: str) -> None:
        """Destroy target database"""
        self.connect.execute(f"DROP TABLE IF EXISTS {db_name};")
        # self.video_connect.execute(f"ALTER TABLE {db_name} AUTO_INCREMENT=1")
        self.connect.commit()

    def destroy_this(self) -> None:
        """Destroy `videos` database and linked delete `video_fts`"""
        self.connect.execute(f"DROP TABLE IF EXISTS videos;")
        # Chain Deletion (recommend)
        self.connect.execute(f"DROP TABLE IF EXISTS videos_fts;")
        self.connect.commit()
