import hashlib

class CryptoHasher:
    
    def encrypt_md5(string) -> str:
        """
        md5加密
        :param string: 需要加密的字符串
        :return: 加密后的字符串
        """
        m = hashlib.md5()
        m.update(string.encode("utf-8"))
        return m.hexdigest()

    def encrypt_sha256(string) -> str:
        """
        sha256加密
        :param string: 需要加密的字符串
        :return: 加密后的字符串
        """
        m = hashlib.sha256()
        m.update(string.encode("utf-8"))
        return m.hexdigest()