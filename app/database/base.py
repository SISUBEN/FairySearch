from typing import Any
import abc


class Database(metaclass=abc.ABCMeta):
    @abc.abstractmetho
    def __init__(self) -> None: ...
    
    # @abc.abstractmethod
    # def __del__(self) -> None: ...
    
    @abc.abstractmethod
    def init(self) -> None: ...
    
    def query(self) -> Any: ...
    
    def get(self) -> Any: ...
    
    def insert(self) -> Any: ...
    
    def __del__(self):
        if hasattr(self, 'connect') and self.connect:
            self.connect.commit()
            self.connect.close()
            del self.connect