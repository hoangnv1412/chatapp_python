import sqlite3
from user_model import UserModel
from time import *

class UserAuthen: 
    __conn = sqlite3.connect("week4.db")
    __c = __conn.cursor()
    __user_model = UserModel()
    def __init__(self,username,password=""):
        self.__username = username
        self.__password = password
        
    def checkAuthen(self):
        query = "SELECT * FROM USER WHERE USER.username = '{0}' AND USER.password = '{1}'".format(self.__username,self.__password)
        self.__c.execute(query)
        values = self.__c.fetchone()
        if (values != None) : 
            self.__user_model = UserModel(values[1],values[2],values[3],values[4],values[5])
            return 1
        else:
            return 0
    def signUp(self,user_model = UserModel()):
        query = "INSERT INTO USER (username,password,name,DOB,sex) " \
		            "VALUES({0},{1},{2},{3},{4})".format(user_model.username,user_model.get_pw,user_model.get_dob,user_model.get_sex)
        self.__c.execute(query)
        self.__conn.commit()

    def getUserInfo(self):
        return self.__user_model
    

class UserManager(UserAuthen):
    __conn = sqlite3.connect("week4.db")
    __c = __conn.cursor()
    def __init__(self,user_model):
        self.__usermodel = user_model
        
    
    def __select_SQLite(self,query,num=0):
        self.__c.execute(query)
        if num == 1:
            values = self.__c.fetchone()
        else: 
            values = self.__c.fetchall()
        return values

    def __insert_SQLite(self,query):
        self.__c.execute(query)
        self.__conn.commit()

    def closeDb(self):
        self.__conn.close()

    def showMes(self):
        query = "SELECT MESSAGE.* FROM MESSAGE,USER WHERE USER.username = '{0}';".format(self.__usermodel.username)
        return self.__select_SQLite(query)
    def isExisted(self,person):
        query = "SELECT * FROM USER WHERE USER.username = '{0}'".format(person)
        values = self.__select_SQLite(query,1)
        if (values != None) : 
            return 1
        else:
            return 0
    def isBlocked(self,person):
        query = "SELECT relation.relation FROM relation "\
            "WHERE (relation.user1 = '{0}' "\
            "AND relation.user2 = '{1}') ".format(self.__usermodel.username,person)
        values = self.__select_SQLite(query,1)
        if (values[0] == 2) : 
            return 1
        else:
            return 0

    def sendMes(self,receiver,content):
        if self.isExisted(receiver):  
            if not self.isBlocked(receiver):
                real_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                query = "INSERT INTO MESSAGE (sender,receiver,content,time) " \
		            "VALUES('" + self.__usermodel.username + "','" + receiver + "','" + content + "','" + real_time + "')"
                self.__insert_SQLite(query)
                print("Sent message successfully")
                
            else: print("ERROR: You blocked user with username = {0}".format(receiver))
        else: print("ERROR: user does not exist")
    def addFriend(self):
        return 0
    def showFriendList(self):
        query = "SELECT a.username FROM USER as a, RELATION as b" \
		" WHERE b.user1 = '{0}' "\
		" AND a.username = b.user2 " \
        " AND b.relation = 1 "\
		" ORDER BY a.username".format(self.__usermodel.username)
        return self.__select_SQLite(query)

    def groupByCity(self):
        query = "SELECT a.username,c.province  FROM USER as a, RELATION as b, ADDRESS as c" \
		    " WHERE b.user1 = '{0}' "\
		    " AND c.username = b.user2 AND a.username = b.user2 "\
            " AND b.relation = 1"\
		    " ORDER BY c.province;".format(self.__usermodel.username)
        return self.__select_SQLite(query)
       
    def getChatHistory(self,person):
        query = "SELECT b.sender,b.receiver,b.content FROM message as b " \
		    " WHERE(b.sender = {0} AND b.receiver = '{1}')" \
		    " OR (b.receiver = '{0}' AND b.sender = '{1}')" \
		    " ORDER BY b.time;"
        return self.__select_SQLite(query)
        
    def getAllUsers(self):
        query = "SELECT USER.username from USER"
        return self.__select_SQLite(query)