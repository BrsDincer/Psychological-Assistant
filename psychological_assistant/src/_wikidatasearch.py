import wikipedia as wpp
from src._errorsinit import *
from src._classinits import *
from llama_index import Document
from typing import Any
import os

class WIKIDATASEARCH(object):
    def __init__(self)->CLASSINIT:
        self.__base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                   "data")
        self.__dir = self.__base+"/wikitargetlist.txt"
        self.targetcontent = []
    def __str__(self)->str:
        return "WIKI DATA SEARCH - SUBPROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->CLASSINIT:
        raise TypeError("[DENIED - PERMISSION]")
    def __repr__(self)->str:
        return WIKIDATASEARCH.__doc__
    def _GETTITLE(self)->RESPONSES:
        with open(self.__dir,"r",errors="ignore",encoding="utf-8") as ff:
            tp = ff.readlines()
        return tp
    def _SEARCH(self,
                mx:int=10,
                **load_kwargs:Any)->RESPONSES:
        # tp = self._GETTITLE()[:4] # FOR TEST
        tp = self._GETTITLE()
        for x_ in tp:
            l_ = wpp.search(x_.replace("\n",""),
                            results=mx)
            if len(l_) != 0:
                for xl_ in l_:
                    try:
                        self.targetcontent.append(Document(wpp.page(str(xl_),
                                                                    **load_kwargs).content))
                    except wpp.exceptions.DisambiguationError:
                        pass
                    except Exception:
                        pass