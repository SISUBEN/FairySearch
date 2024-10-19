import re

class RegExr:
    def __init__(self, regex):
        self.regex = regex

    def validate(self, value):
        if re.match(self.regex, value):
            return True
        return False

class Email(RegExr):
    def __init__(self):
        super().__init__(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')

class Password(RegExr):
    def __init__(self):
        super().__init__(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}$')
        
class Username(RegExr):
    def __init__(self):
        super().__init__(r'^[a-zA-Z][a-zA-Z0-9_]{4,15}$')
        
# 匹配正则表达式
email = Email()
print(email.validate('example@example.com'))
