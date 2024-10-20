import time
from datetime import datetime

class TimeKeeper:
    def datatime(timestamp: int|float) -> str:
        """Convert timestamp to datetime

        Args:
            timestamp (float): timestamp

        Returns:
            str: datetime YY-MM-DD HH:MM:SS
        """
        return time.strftime('%Y-%m-%d %H:%M:%S', timestamp)
    
    def timestamp(_datetime: str) -> float:
        """Convert datetime to timestamp

        Args:
            datetime (str): current datetime YY-MM-DD HH:MM:SS

        Returns:
            float: timestamp
        """
        return datetime.timestamp(_datetime)
    
    def get_timestamp() -> float:
        """Get current timestamp

        Returns:
            float: timestamp
        """
        return time.time()
    
    def get_datetime() -> str:
        """Get current datetime

        Returns:
            datetime: 
        """
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')