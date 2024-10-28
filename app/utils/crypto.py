import hashlib
class CryptoHasher(object):
    def __init__(self) -> None:
        self.encoding = "utf-8"
    
    def md5(self, string: str) -> str:
        """
        md5 encryption
        :param string: plain
        :return: cipher length 32
        """
        m = hashlib.md5()
        m.update(string.encode(self.encoding))
        return m.hexdigest()

    def sha256(self, string: str) -> str:
        """
        sha256 encryption
        :param string: plain
        :return: cipher length 64
        """
        m = hashlib.sha256()
        m.update(string.encode("utf-8"))
        return m.hexdigest()