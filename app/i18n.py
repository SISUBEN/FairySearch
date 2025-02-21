import os
import gettext
import threading
import locale
thread = threading.Thread()
dir = os.path.dirname(os.path.abspath(__file__))
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
        # locale_lang = "en_US"
        self.trans = gettext.translation(domain='messages', localedir="locales", languages=[language or locale_lang], fallback=True)
    
    def translate(self, text: str):
        return self.trans.gettext(text)
    
    def set_language(self, language: str):
        self.trans = gettext.translation(domain='messages', localedir="locales", languages=[language], fallback=True)
        
        
t = Translate(language="en_US")
_ = t.translate
