class UserModel(object):
    def __init__(self, Username="", Pw="", Name="", Dob="", Sex=0, Address=0):
        self.username = Username
        self.__pw = Pw
        self.name = Name
        self.__dob = Dob
        self.__sex = Sex
        self.__address = Address

    #getter
    def get_pw(self):
        return self.__pw
    def get_dob(self):
        return self.__dob
    def get_sex(self):
        return self.__sex
    def get_address(self):
        return self.__address

    #setter
    def set_name(self,name):
        self.name = name
    def setPw(self,pw):
        self.__pw = pw
    def setDob(self,dob):
        self.__dob = name
    def setSex(self,sex):
        self.__sex = name
    def setAddress(self,address):
        self.__address = name