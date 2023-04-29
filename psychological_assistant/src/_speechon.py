from src._classinits import *
import pyttsx3

class SPEECHON(object):
    def __init__(self)->CLASSINIT:
        self.__e = pyttsx3.init()
    def __str__(self)->str:
        return "SPEECH ON - SUBPROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->CLASSINIT:
        raise TypeError("[DENIED - PERMISSION]")
    def __repr__(self)->str:
        return SPEECHON.__doc__
    def _RUN(self,tx:str)->RESPONSES:
        sr_ = self.__e.getProperty("rate")
        vl_ = self.__e.getProperty("volume")
        self.__e.setProperty("volume",vl_+1.30)
        if int(sr_) >= 250:
            self.__e.setProperty("rate", int(sr_)-100)
        elif 180 <= int(sr_) <= 220:
            self.__e.setProperty("rate", int(sr_)-75)
        elif int(sr_) <= 180:
            self.__e.setProperty("rate", int(sr_)-45)
        else:
            pass
        self.__e.say(str(tx))
        self.__e.runAndWait()