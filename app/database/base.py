from typing import Any
import abc
class Database(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self) -> None: ...
    @abc.abstractmethod
    def init(self) -> None: ...
    @abc.abstractmethod
    def query(self) -> Any: ...
    @abc.abstractmethod
    def get(self) -> Any: ...
    @abc.abstractmethod
    def insert(self) -> Any: ...
    @abc.abstractmethod
    def __del__(self) -> None: ...
    # def __init_subclass__(cls: Any, **kwargs) -> None:
    #     "At least implement get() or query()"
    #     super().__init_subclass__(**kwargs)
    #     if not (cls.get is not Database.get or cls.query is not Database.query):
    #         raise TypeError(
    #             f"{cls.__name__} must implement at least one of get or query"
    #         )