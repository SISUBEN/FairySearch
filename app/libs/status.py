from app.database.queries import Database
from app.libs.expection import NoLoginError
db = Database

class Status:
    def __init__(self) -> None:
        self.__login = None
    
    def set_login(self, login: bool) -> None:
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
            raise NoLoginError
        return db.userdb.query_user_uid(self.__login)
    
    def __str__(self) -> str:
        return str(self.__login)