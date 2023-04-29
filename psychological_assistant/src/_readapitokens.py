from src._classinits import *
from src._errorsinit import *
import os

class READAPITOKEN(object):
    def __init__(self)->CLASSINIT:
        self.token = None
        self.__base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                   "data")
        self.__dir = self.__base+"/tokeninit.txt"
    def __str__(self)->str:
        return "READ API TOKEN - SUBPROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->CLASSINIT:
        raise TypeError("[DENIED - PERMISSION]")
    def __repr__(self)->str:
        return READAPITOKEN.__doc__
    def _TOKEN(self)->RESULTS:
        try:
            with open(self.__dir,"r") as ff:
                self.token = ff.read()
        except:
            FILEERROR().print()