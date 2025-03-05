import os
import gettext
import threading
import locale
# from app.modules.assets.
thread = threading.Thread()
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "locale")
# i18n_file_path = os.path.join(dir, "locales")
# print("domain",gettext.textdomain(domain=None))
class Translate:
    def __init__(self, language: str|int = 0) -> None:
        """__init__
            init i18n translator
        Args:
            language (str | int, optional): str for req language, int for automatic detect. Defaults to 0.
        """        
        locale_lang = locale.getlocale()[0]
        language = locale_lang if language == 0 else language
        # language = "en_US"
        self.trans = gettext.translation(domain='messages', localedir=FILE_PATH, languages=[language], fallback=True)
        self.trans.install()
    
    def translate(self, text: str):
        return self.trans.gettext(text)
    
    def set_language(self, language: str):
        self.trans = gettext.translation(domain='messages', localedir=FILE_PATH, languages=[language], fallback=True)
        self.trans.install()
        
        
t = Translate()
_ = t.translate
