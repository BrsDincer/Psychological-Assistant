class NETWORKERROR(object):
    n_ = "[NETWORK ERROR - CHECK YOUR INTERNET CONNECTION]"
    def print(self):
        print("ERROR TYPE: %s"%self.n_)
class PACKAGEERROR(object):
    n_ = "[PACKAGE ERROR - CHECK RESOURCES OF REQUIRED LIBRARIES]"
    def print(self):
        print("ERROR TYPE: %s"%self.n_)
class INITERROR(object):
    n_ = "[SYSTEM ERROR - CHECK YOUR SYSTEM AND REQUIREMENTS]"
    def print(self):
        print("ERROR TYPE: %s"%self.n_)
class FILEERROR(object):
    n_ = "[FILE ERROR - CHECK YOUR FILE DIRECTORIES]"
    def print(self):
        print("ERROR TYPE: %s"%self.n_)