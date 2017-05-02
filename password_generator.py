import uuid
import random

SYMBOL = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

class PasswordGenerator:
    """
    Generate a password that is either strong or weak.
    """
    def __init__(self):
        self.Password = ""
        
    def generate_password(self, strength):
    """
    (str) -> (str)
    Input of weak or strong, builds and returns password accordingly.
    """
        if strength == 'weak':
            return self.__generate_weak_password()
        elif strength == 'strong':
            return self.__generate_strong_password()
        else:
            return "Not a password strength"
            
    def __generate_weak_password(self):
    """
    -> (str)
    Returns a uuid4 as the password
    """
        return str(uuid.uuid4())[:8]

    def __generate_strong_password(self):
    """
    -> (str)
    Returns a password that includes uppcase, lowercase and symbols.
    Randomly generated from a UUID4 to begin with.
    """
        base = str(uuid.uuid4())[:16]
        countUppers = 0
        for i in range(0,16):
            if countUppers % 2:
                base = base[:i] + base[i].upper() + base[i:]
            elif countUppers % 3:
                base = base[:i] + self.__random_symbol() + base[i:]
            countUppers += 1

        return base

    def __random_symbol(self):
    """
    -> (str)
    Returns a random symbol from the list above.
    """
        return SYMBOL[random.randint(0,9)]
