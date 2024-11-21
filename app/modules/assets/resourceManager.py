# import dataclass
from dataclasses import dataclass
import os


@dataclass
class ResouceManager:
    current_dir: str = os.path.dirname(os.path.abspath(__file__))
    covers_dir: str = os.path.join(current_dir, "covers")
    videos_dir: str = os.path.join(current_dir, "videos")

    def getVideo(self, vid: int, file_type: str = "mp4") -> str:
        """get video file path

        Args:
            vid (int): video id
            file_type (str, optional): type of file. Defaults to "mp4".

        Returns:
            _type_: video file path
        """
        if os.path.exists(p := os.path.join(self.videos_dir, f"{vid}.{file_type}")):
            return p
        else:
            return None

    def getCover(self, vid: int, file_type: str = "png") -> str:
        """get cover file path
        
        Args:
            vid (int): video id
            file_type (str, optional): type of file. Defaults to "png".

        Returns:
            _type_: cover file path
        """
        if os.path.exists(p := os.path.join(self.covers_dir, f"{vid}.{file_type}")):
            return p
        else:
            return None
