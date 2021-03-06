class ProvinceModel:
    def __init__(self,Code=0):
        self.__code = Code
    def num(self):
        return 64
    def convert_to_name(self,x):
        x = str(x)
        return {
        "1" : "An Giang",
        "2" : "Ba Ria - Vung Tau",
        "3" : "Bac Lieu",
        "4" : "Bac Kan",
        "5" : "Bac Giang",
        "6" : "Bac Ninh",
        "7" : "Ben Tre",
        "8" : "Binh Duong",
        "9" : "Binh Dinh",
        "10" : "Binh Phuoc",
        "11" : "Binh Thuan",
        "12" : "Ca Mau",
        "13" : "Cao Bang",
        "14" : "Can Tho(TP)",
        "15" : "Da Nang(TP)",
        "16" : "Dak Lak",
        "17" : "Dak Nong",
        "18" : "Dien Bien",
        "19" : "Dong Nai",
        "20" : "Dong Thap",
        "21" : "Gia Lai",
        "22" : "Ha Giang",
        "23" : "Ha Nam",
        "24" : "Ha Noi(TP)",
        "25" : "Ha Tay",
        "26" : "Ha Tinh",
        "27" : "Hai Duong",
        "28" : "Hai Phong(TP)",
        "29" : "Hoa Binh",
        "30" : "Ho Chi Minh(TP)",
        "31" : "Hau Giang",
        "32" : "Hung Yen",
        "33" : "Khanh Hoa",
        "34" : "Kien Giang",
        "35" : "Kon Tum",
        "36" : "Lai Chau",
        "37" : "Lao Cai",
        "38" : "Lang Son",
        "39" : "Lam Dong",
        "40" : "Long An",
        "41" : "Nam Dinh",
        "42" : "Nghe An",
        "43" : "Ninh Binh",
        "44" : "Ninh Thuan",
        "45" : "Phu Tho",
        "46" : "Phu Yen",
        "47" : "Quang Binh",
        "48" : "Quang Nam",
        "49" : "Quang Ngai",
        "50" : "Quang Ninh",
        "51" : "Quang Tri",
        "52" : "Soc Trang",
        "53" : "Son La",
        "54" : "Tay Ninh",
        "55" : "Thai Binh",
        "56" : "Thai Nguyên",
        "57" : "Thanh Hoa",
        "58" : "Thua Thien-Hue",
        "59" : "Tien Giang",
        "60" : "Tra Vinh",
        "61" : "Tuyen Quang",
        "62" : "Vinh Long",
        "63" : "Vinh Phuc",
        "64" : "Yen Bai"
        }[x]



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


#class MessageModel:
