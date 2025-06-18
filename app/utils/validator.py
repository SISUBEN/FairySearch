import re

class RegExr:
    def __init__(self, regex):
        self.regex = regex

    def validate(self, value) -> bool:
        """
        Validates the given value against a predefined regular expression.
        Args:
            value (str): The input value to validate.
        Returns:
            bool: True if the value matches the regular expression, False otherwise.
        Example:
            ```python
            email = Email()  
            email.validate("example@example.com")
            ```
            >>> True
        """
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
        
class KeyPath(RegExr):
    def __init__(self):
        super().__init__(r'^[a-zA-Z0-9|\_]+\.[a-zA-Z0-9|\_]+$')
        