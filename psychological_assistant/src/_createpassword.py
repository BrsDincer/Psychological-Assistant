import random,string
from src._classinits import *

class RANDOMPASSWORD(object):
    def __init__(self)->CLASSINIT:
        self.password = None
        self.username = None
    def __str__(self)->str:
        return "CREATING RANDOM PASSWORD - SUBPROCESS"
    def __call__(self)->None:
        return None
    def __gestate__(self)->CLASSINIT:
        raise TypeError("[DENIED - PERMISSION]")
    def __repr__(self)->str:
        return RANDOMPASSWORD.__doc__
    def _GET(self)->RESULTS:
        r_ = string.ascii_letters+string.digits+string.punctuation
        p_ = random.choices(string.ascii_lowercase,k=3)
        p_ += random.choices(string.digits,k=3)
        p_ += random.choices(string.punctuation,k=2)
        p_ += random.choices(string.ascii_uppercase,k=3)
        p_ += random.choices(string.digits,k=2)
        p_ += random.choices(string.punctuation,k=2)
        p_ += random.choices(string.ascii_lowercase,k=3)
        p_ += random.choices(string.punctuation,k=2)
        p_ += random.choices(string.ascii_uppercase,k=3)
        p_ += random.choices(r_,k=4)
        self.password = "".join(p_)
        self.username = self.password[:6]
    def _PRINT(self)->RESPONSES:
        print(f"\n\nPLEASE USE YOUR CREDENTIALS TO ACCESS\n\nYOUR USERNAME: {self.username}\nYOUR PASSWORD: {self.password}\n\n")