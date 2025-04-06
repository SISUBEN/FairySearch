from .db_config import Config
from app.database.base import Database
from app.utils.crypto import CryptoHasher
from app.utils.logger.logger import logger
import sqlite3

class Userdb(Database):
    def __init__(self) -> None:
        self.cryptor = CryptoHasher()
        self.connect = sqlite3.connect(Config.PATHS.get("user_db"))
        self.INIT_USER_DB_SQL = Config.load(Config.PATHS.get("init_user_db_sql"))
        self.init()

    def init(self) -> None:
        try:
            self.connect.execute(self.INIT_USER_DB_SQL)
            self.connect.commit()
        except sqlite3.Error as e:
            logger.debug(f"init user db fail: {e}")
            self.connect.rollback()

    def insert(self, username: str, password: str) -> str:
        """Add user to database with token (a shortcut of create_user)

        Args:
            username (str): username
            password (str): password must be plain text

        Returns:
            str: user's token
            
        """
        return self.create_user(username, password)  
    
    def create_user(self, username: str, password: str) -> str:
        """Add user to database with token

        Args:
            username (str): username
            password (str): password must be plain text

        Returns:
            str: user's token
        
        """
        try:
            encrypted = self.cryptor.sha256(password)
            token = self.generate_token(username, encrypted)
            self.connect.execute(Config.USER_ADD, (username, encrypted, token))
            self.connect.commit()
            return token
        except sqlite3.Error as e:
            logger.debug(f"add user token fail: {e}")
            self.connect.rollback()
        except Exception as e:
            logger.debug(f"create token fail: {e}")

    def verify_token(self, token: str) -> bool:
        """Verify token

        Args:
            token (str): token

        Returns:
            bool: is True if token is valid
        """
        try:
            return (
                self.connect.execute(Config.USER_QUERY, (token,)).fetchone()
                is not None
            )
        except sqlite3.Error as e:
            logger.debug(f"verify token error: {e}")

    def get_token(self, username: str) -> str:
        """Get token by username

        Args:
            username (str): username

        Returns:
            str: token

        Exception:
            sqlite3.Error: if error occurs
        """
        try:
            return self.connect.execute(
                Config.USER_QUERY, (username,)
            ).fetchone()[0][0]
        except sqlite3.Error as e:
            logger.debug(f"get token error: {e}")

    def generate_token(self, username: str, password: str) -> str:
        """Generate token for user

        Args:
            username (str): username plain text
            password (str): password cipher text

        Raises:
            Exception: if user not exists

        Returns:
            str[64]: token (a sha256 hash)
        """
        token = {
            "username": username,
            "pasword": password,
        }
        token = str(token)
        return self.cryptor.sha256(token)

    def is_user_exists(self, username: str) -> bool:
        """Check if user exists

        Args:
            username (str): username

        Returns:
            bool: is Ture if user exists

        Exception:
            sqlite3.Error: if error occurs
        """
        try:
            return (
                self.connect.execute(Config.USER_QUERY_EXISTS, (username,)).fetchone()
                is not None
            )  # if query result is not None, return True, else return result
        except sqlite3.Error as e:
            logger.debug(f"An error occurred when querying user exists: {e}")

    def get_username(self, token: str) -> list:
        """get username by token

        Args:
            token (str): login token

        Returns:
            str: username
        """
        try:
            return self.connect.execute(
                Config.USERNAME_QUERY, (token,)
            ).fetchall()[0][0]
        except sqlite3.Error as e:
            logger.debug(f"query username error: {e}")

    def destroy_db(self, db_name: str) -> None:
        try:
            self.connect.execute(f"DROP TABLE IF EXISTS {db_name};")
            self.connect.commit()
        except sqlite3.Error as e:
            logger.debug(f"destroy db fail: {e}")

    def __get_user_password(self, username: str) -> str:
        """Query user password by username

        Args:
            username (str): username

        Returns:
            str: user password
        """
        try:
            return self.connect.execute(
                Config.USER_QUERY_PWD_BY_USRNAME, (username,)
            ).fetchall()[0][0]
        except sqlite3.Error as e:
            logger.debug(f"query user password error: {e}")
        except IndexError:
            logger.debug(f"query user password error: {username} not exists")

    def get(self, token: str) -> int:
        """Get user uid by token

        Args:
            token (str): login token

        Returns:
            int: user uid

        Exception:
            sqlite3.Error: if query fail
        """
        try:
            return self.connect.execute(
                Config.USER_QUERY_UID, (token,)
            ).fetchall()[0][0]
        except sqlite3.Error as e:
            logger.debug(f"get uid error: {e}")

    def query(self) -> None: ...

    def verify_user(self, password: str, username: str) -> bool:
        """Verfy user password

        Args:
            password (str): user password (encrypted)
            username (str): username

        Returns:
            bool: True if password is correct, False otherwise
        """
        return self.__get_user_password(username) == password
