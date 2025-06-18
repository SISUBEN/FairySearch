from enum import Enum
import os
import yaml
from PySide6.QtCore import QFile, QTextStream
from dataclasses import dataclass
from app.utils.logger.logger import logger
from app.utils.validator import KeyPath
from app.assets import resources_rc

logger.debug(f"Current file dir: {os.getcwd()}")


class Default(Enum):
    DEFAULT_COVER = ":/covers/covers/default.png"


@dataclass
class Config:
    def __init__(self):
        create_db = False
        # path check
        for path in self.PATHS["db"]:
            if os.path.isfile(self.PATHS["db"][path]) is False:
                logger.error(f"Database file not found: {self.PATHS['db'][path]}")
                create_db = True
        for path in self.PATHS["qrc"]:
            if Config.qrc_path_check(self.PATHS["qrc"][path]) is False:
                logger.fatal(
                    f"Fatal Error: \n\tResource file not found: {self.PATHS['qrc'][path]}\n\t# Resource File Incompleted"
                )
        if create_db is True:
            logger.info("Database file not found, creating new database...")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    # locate database path automatically
    # Database sql path

    def create_db(self) -> None:
        "Creates the database files if they do not exist."
        os.path.isdir(os.path.join(self.current_dir, "db")) or os.mkdir(
            os.path.join(self.current_dir, "db")
        )
        for _, path in self.PATHS["db"]:
            if os.path.isfile(path) is False:
                open(path, "w").close()

    def path_check(self, path: str) -> bool:
        """
        Checks if the given path exists and is a file.
        Args:
            path (str): The path to check.
        Returns:
            bool: True if the path exists and is a file, False otherwise.
        """
        return os.path.isfile(path)

    @staticmethod
    def qrc_path_check(resource_path: str) -> bool:
        """
        Checks if QRC file path exists and can be opened in read-only text mode.
        Args:
            resource_path (str): The path to the resource file.
        Returns:
            bool: True if the file exists and can be opened in read-only text mode, False otherwise.
        """
        file = QFile(resource_path)
        if not file.open(QFile.ReadOnly | QFile.Text):
            file.close()
            return False
        file.close()
        return True
        

    @staticmethod
    def load(resource_path: str) -> str:
        """
        Loads the content of a resource file as a string.
        Args:
            resource_path (str): The file path to the resource file.
        Returns:
            str: The content of the resource file.
        Raises:
            FileNotFoundError: If the resource file cannot be opened.
        """
        file = QFile(resource_path)
        if not file.open(QFile.ReadOnly | QFile.Text):
            logger.error(f"Cannot open resource file: {resource_path}")
            raise FileNotFoundError(f"Cannot open resource file: {resource_path}")
        stream = QTextStream(file)
        content = stream.readAll()
        file.close()
        return content

    PATHS = {
        "db": {
            "video_db": os.path.join(current_dir, "db", "videos.db"),
            "user_db": os.path.join(current_dir, "db", "users.db"),
        },
        "qrc": {
            "import_data_sql": r":/data_sql/sql/import_data.sql",
            "video_activity_data_sql": r":/table_sql/sql/video_activity_data.sql",
            "init_video_db_sql": r":/table_sql/sql/init_video_db.sql",
            "init_user_db_sql": r":/table_sql/sql/init_user_db.sql",
            "init_search_history_db_sql": r":/table_sql/sql/init_search_history_db.sql",
            "init_fts_sql": r":/table_sql/sql/init_fts.sql",
            "triggers_sql": r":/table_sql/sql/triggers.sql",
            "queries_sql": r":/table_sql/sql/queries.yaml",
        },
    }

    @classmethod
    def get_path(cls, path: str) -> str:
        db = cls.PATHS.get("db").get(path)
        qrc = cls.PATHS.get("qrc").get(path)
        if db is None and qrc is None:
            raise ValueError(f"Invalid path: {path}")
        else:
            return db if db is not None else qrc


class DatabaseQueryManager:
    _queries = None
    _validator = KeyPath()

    @classmethod
    def load_queries(cls):
        path = Config.get_path("queries_sql")
        cls._queries = yaml.safe_load(Config.load(path))

    @classmethod
    def get_query(cls, key_path: str) -> str:
        """
        Retrieves a query string from the stored queries using a dot-separated key path.
        Args:
            key_path (str): A dot-separated string representing the path to the desired query
                            within the nested query structure.
        Returns:
            str: The query string corresponding to the provided key path.
        Raises:
            ValueError: If the key path is invalid or does not conform to the expected format.
        Example:
            ```python
            DatabaseQueryManager.get_query("user.user_add")
            >>> "INSERT INTO users (username, password, token) VALUES (?, ?, ?);"
            ```
        """

        if cls._queries is None:
            cls.load_queries()
        if not cls._validator.validate(key_path):
            raise ValueError(f"Invalid key path: {key_path}")

        path_parts = key_path.split(".")
        result = cls._queries
        for part in path_parts:
            logger.debug(f"part: {part}")
            if part in result:
                result = result[part]
            else:
                raise KeyError(f"Query key '{key_path}' not found in queries")

        return result
