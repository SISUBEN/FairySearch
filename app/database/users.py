import sqlite3
from .db_config import Config
from app.utils.crypto import CryptoHasher
from app.utils.logger.logger import logger
cryptor = CryptoHasher()

class Userdb:
        def __init__(self) -> None:
            self.user_connect = sqlite3.connect(Config.PATHS["user_db"])
            self.user_cur = self.user_connect.cursor()
            self.INIT_USER_DB_SQL = Config.load(Config.PATHS["init_user_db_sql"])
            self.init_userdb()

        def init_userdb(self) -> None:
            try:
                self.user_connect.execute(self.INIT_USER_DB_SQL)
                self.user_connect.commit()
            except sqlite3.Error as e:
                logger.debug(f"init user db fail: {e}")
                self.user_connect.rollback()
                
        def user_add(self, username: str, password: str) -> None:
            try:
                self.user_connect.execute(Config.USER_ADD, (username, password))
                self.user_connect.commit()
            except sqlite3.Error as e:
                logger.debug(f"add user fail: {e}")
                self.user_connect.rollback()

        def t_user_add(self, username: str, password: str) -> str:
            """Add user to database with token

            Args:
                username (str): username
                password (str): password must be plain text
            """
            try:
                encrypted = cryptor.sha256(password)
                token = self.generate_token(username, encrypted)
                self.user_connect.execute(Config.T_USER_ADD, (username, encrypted, token))
                self.user_connect.commit()
                return token
            except sqlite3.Error as e:
                logger.debug(f"add user token fail: {e}")
                self.user_connect.rollback()
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
                return self.user_connect.execute(Config.T_USER_QUERY, (token,)).fetchone() is not None
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
                 return self.user_connect.execute(Config.T_USER_QUERY, (username,)).fetchone()[0][0]
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
            return cryptor.sha256(token)
                
        
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
                    self.user_connect.execute(Config.USER_QUERY, (username,)).fetchone()
                    is not None
                ) # if query result is not None, return True, else return result
            except sqlite3.Error as e:
                logger.debug(f"An error occurred when querying user exists: {e}")
        
        def query_username(self, token: str) -> list:
            """query username by token

            Args:
                token (str): login token

            Returns:
                str: username
            """
            try:
                return self.user_connect.execute(Config.T_USERNAME_QUERY, (token,)).fetchall()[0][0]
            except sqlite3.Error as e:
                logger.debug(f"query username error: {e}")

        def destroy_db(self, db_name: str) -> None:
            try:
                self.user_connect.execute(f"DROP TABLE IF EXISTS {db_name};")
                self.user_connect.commit()
            except sqlite3.Error as e:
                logger.debug(f"destroy db fail: {e}")
                
        def query_user_password(self, username: str) -> str:
            """Query user password by username

            Args:
                username (str): username

            Returns:
                str: user password
            """
            try:
                return self.user_connect.execute(Config.USER_QUERY_PWD, (username,)).fetchall()[0][0]
            except sqlite3.Error as e:
                logger.debug(f"query user password error: {e}")
                
        def query_user_uid(self, username: str) -> int:
            """Query user uid by username

            Args:
                username (str): username

            Returns:
                int : user uid
                
            Exception:
                sqlite3.Error: if query fail
            """
            try:
                return self.user_connect.execute(Config.USER_QUERY_UID, (username,)).fetchall()[0][0]
            except sqlite3.Error as e:
                logger.debug(f"query user uid error: {e}")

        def query_uid(self, token: str) -> int:
            """Query user uid by token

            Args:
                token (str): login token

            Returns:
                int: user uid
                
            Exception:
                sqlite3.Error: if query fail
            """
            try:
                return self.user_connect.execute(Config.T_USER_QUERY_UID, (token,)).fetchall()[0][0]
            except sqlite3.Error as e:
                logger.debug(f"query uid error: {e}")
        
        def verify_user(self, password: str, username: str) -> bool:
            """Verfy user password

            Args:
                password (str): user password (encrypted)
                username (str): username

            Returns:
                bool: True if password is correct, False otherwise
            """
            return self.query_user_password(username) == password

        def __del__(self) -> None:
            self.user_connect.close()