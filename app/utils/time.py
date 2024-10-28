import time
from datetime import datetime
from app.modules.logger.logger import logger
from functools import wraps
# Author: Vertin
# Date: 1999

class TimeKeeper:
    def __init__(self) -> None:
        self.date_format = '%Y-%m-%d %H:%M:%S'
    
    def datetime(self, timestamp: int|float) -> str:
        """Convert timestamp to datetime

        Args:
            timestamp (float): timestamp

        Returns:
            str: datetime YY-MM-DD HH:MM:SS
        """
        return time.strftime(self.date_format, time.localtime(timestamp))
    
    def timestamp(self, _datetime: str) -> float:
        """Convert datetime to timestamp

        Args:
            datetime (str): current datetime YY-MM-DD HH:MM:SS

        Returns:
            float: timestamp
        """
        return datetime.timestamp(_datetime)
    
    def get_timestamp(self) -> float:
        """Get current timestamp

        Returns:
            float: timestamp
        """
        return time.time()
    
    def get_datetime(self) -> str:
        """Get current datetime

        Returns:
            datetime: 
        """
        return datetime.now().strftime(self.date_format)
    
    @staticmethod
    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            logger.info(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
            return result
        return wrapper