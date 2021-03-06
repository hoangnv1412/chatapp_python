import sqlite3
from models import UserModel
from time import *

#Class dbManager:
    #for connect and query db file
    #method:
        #connectDb : for connecting database file
        #select_SQLite : for select queries 
        #queries_SQLite : for other kinds of queries 

#Class UserAuthen
    #for sign_in and sign_up, and get user information
    #methods:
        #checkAuthen: check for user authentication, return 1 if login successfully, 0 for others
        #signup: for sign up
        #getUserInfo: return user info in UserModel-object-type

#Class UserManager:
    #for user acts after signing in
    #methods:
        #showMes: show all messages
        #isExisted(string): return 1 if user exists, 0 if not
        #isBlocked(string): return 1 if user and another account if in a block-relationship, 0 if not 
        #isFriend(string): return 1 if user and another account are friends, 0 if not
        #sendMes(string): send someone messages
        #addfriend(string): add friend someone
        #showFriendList(): show user's all friends
        #Block(string): block someone
        #groupByCity: group user's friends by their addresses
        #getChatHistory(string): get all messages of user with a person
        #getAllUser(): get all system's users

class dbManager:
    def connectDb(self):
        conn = sqlite3.connect("week4.db")
        return conn

    def select_SQLite(self,query,num=0):
        conn = connectDb()
        c = conn.cursor()
        c.execute(query)
        conn.commit()

        if num == 1:
            values = self.__c.fetchone()
        else: 
            values = self.__c.fetchall()
        return values

    def queries_SQLite(self,query):
        conn = self.__connectDb()
        conn.execute(query)
        conn.commit()

    def closeDb(self):
        self.__conn.close()

class UserAuthen(dbManager): 
    
    __user_model = UserModel()

    def __init__(self,username,password=""):
        self.__username = username
        self.__password = password
        
    def checkAuthen(self):
        query = "SELECT * FROM USER WHERE USER.username = '{0}' AND USER.password = '{1}'".format(self.__username,self.__password)
        values = self.select_SQLite(query)
        if (values != None) : 
            self.__user_model = UserModel(values[1],values[2],values[3],values[4],values[5])
            return 1
        else:
            return 0

    def signUp(self,user_model = UserModel()):
        query = "INSERT INTO USER (username,password,name,DOB,sex) " \
		            "VALUES({0},{1},{2},{3},{4})".format(user_model.username,user_model.get_pw,user_model.get_dob,user_model.get_sex)
        self.queries_SQLite(query)

    def getUserInfo(self):
        return self.__user_model
    

class UserManager(dbManager):
    def __init__(self,user_model):
        self.__usermodel = user_model

    def showMes(self):
        query = "SELECT MESSAGE.* FROM MESSAGE,USER WHERE USER.username = '{0}';".format(self.__usermodel.username)
        return self.select_SQLite(query)
    def isExisted(self,person):
        query = "SELECT * FROM USER WHERE USER.username = '{0}'".format(person)
        values = self.select_SQLite(query,1)
        if (values != None) : 
            return 1
        else:
            return 0
    def isBlocked(self,person):
        query = "SELECT RELATION.relation FROM RELATION as a "\
            "WHERE (a.user1 = '{0}' "\
            "AND a.user2 = '{1}') "\
            "OR (a.user1 = '{1}' "\
            "AND a.user2 = '{0}')".format(self.__usermodel.username,person)
            
        values = self.select_SQLite(query,1)
        if (values[0] == 2) : 
            return 1
        else:
            return 0


    def sendMes(self,receiver,content):
        if self.isExisted(receiver):  
            if not self.isBlocked(receiver):
                real_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                query = "INSERT INTO MESSAGE (sender,receiver,content,time) " \
		            "VALUES('{0}','{1}','{2}','{3}')".format(self.__usermodel.username,receiver, content,real_time)
                self.queries_SQLite(query)
                return 1

            else: return 0

        else: return 2

    def isFriend(self,person):
        query = "SELECT * FROM FRIEND " \
		"WHERE FRIEND.user1 = '{0}' " \
        "AND FRIEND.user2 = '{1}' ".format(self.__usermodel.username,person)
        value = self.select_SQLite(query,1)
        if (value == None):
            return 0
        return 1

    def addFriend(self,person):
        isBl = self.isBlocked(person)
        isFr = self.isFriend(person)

        if isBl : 
            return 0
        if isFr : 
            return 2

        if (not(isBl) and not(isFr) ) : 
            query = "INSERT INTO RELATION (user1,user2,relation) " \
             "VALUES('{0}','{1}')".format(self.__usermodel.username , person)
            query2 = "INSERT INTO RELATION (user1,user2,relation) " \
             "VALUES('{1}','{0}')".format(self.__usermodel.username , person)
            self.queries_SQLite(query)
            self.queries_SQLite(query2)
            return 1
            

    def showFriendList(self):
        query = "SELECT a.username FROM USER as a, RELATION as b" \
		" WHERE b.user1 = '{0}' "\
		" AND a.username = b.user2 " \
        " AND b.relation = 1 "\
		" ORDER BY a.username".format(self.__usermodel.username)
        return self.select_SQLite(query)

    def groupByCity(self):
        query = "SELECT a.username,c.province  FROM USER as a, RELATION as b, ADDRESS as c " \
		    " WHERE b.user1 = '{0}' "\
		    " AND c.username = b.user2 AND a.username = b.user2 "\
            " AND b.relation = 1 "\
		    " ORDER BY c.province;".format(self.__usermodel.username)
        return self.select_SQLite(query)
       
    def getChatHistory(self,person):
        query = "SELECT b.sender,b.receiver,b.content FROM message as b " \
		    " WHERE(b.sender = '{0}' AND b.receiver = '{1}') " \
		    " OR (b.receiver = '{0}' AND b.sender = '{1}') " \
		    " ORDER BY b.time;".format(self.__usermodel.username,person)
        return self.select_SQLite(query)
        
    def getAllUsers(self):
        query = "SELECT USER.username from USER"
        return self.select_SQLite(query)
    
    def block(self,person,case=0):
        if case == 1:
            query = "UPDATE RELATION "\
               "SET relation = 2 " \
               "WHERE user1 = {0} and user2 = {1} ".format(self.__usermodel.username,person)
            query2 = "DELETE FROM RELATION "\
                "WHERE user1={1} and user2 = {0} ".format(self.__usermodel.username,person)
            self.queries_SQLite(query)
            self.queries_SQLite(query2)
            
        else: 
            query = "INSERT INTO RELATION(user1,user2,relation) "\
                " VALUES({1},{0},2) ".format(self.__usermodel.username,person)
            self.queries_SQLite(query)

            