import hashlib

class CryptoHasher(object):
    def __init__(self) -> None:
        self.encoding = "utf-8"
    
    def encrypt_md5(self, string: str) -> str:
        """
        md5加密
        :param string: 需要加密的字符串
        :return: 加密后的字符串
        """
        m = hashlib.md5()
        m.update(string.encode(self.encoding))
        return m.hexdigest()

    def encrypt_sha256(self, string: str) -> str:
        """
        sha256加密
        :param string: 需要加密的字符串
        :return: 加密后的字符串
        """
        m = hashlib.sha256()
        m.update(string.encode("utf-8"))
        return m.hexdigest()