from app.database.queries import Database
from app.utils.crypto import CryptoHasher
db = Database
cryptor = CryptoHasher()
class Status:
    
    def __init__(self, mode) -> None:
        """_Initialize status class_

        Args:
            mode (int): 0 for safe mode, 1 for danger mode
        """
        self.SAFE = 0
        self.DANG = 1
        self.__login = None
        self.__mode = mode
        self.AUTO_HETCH = True
    
    def set_login(self, login: str) -> None:
        if self.__mode == self.SAFE:
            self.__login = cryptor.sha256(login)
        self.__login = login
        
    def get_login(self) -> bool:
        return self.__login
    
    def get_login_uid(self) -> str:
        """Get Login user's uid
            **must set_login before get_login**
        Raises:
            NoLoginError: if login is None
        Returns:
            str: uid
        """
        if self.__login is None:
            return
        return db.userdb.query_user_uid(self.__login)
    
    def token_generate(self, uid: int , username: str, password: str) -> str:
        """
        generate token
        :param string: plain
        :return: cipher length 64
        """
        user_info = {
            "password": password,
            "username": username
        }
        return cryptor.sha256(str(user_info))
    
    def token_verify(self, token: str, string: str) -> bool:
        """
        verify token
        :param token: cipher
        :param string: plain
        :return: bool
        """
        return cryptor.sha256(string) == token
    
    def __str__(self) -> str:
        return str(self.__login)