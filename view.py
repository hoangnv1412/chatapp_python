
from models import *
from user_manager import *
from msvcrt import getch
#inputkey = ord(getch())

class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

def signup():
    name = input("Enter username : ")
    password = input("Enter password : ")
    re_pw = input("Rewrite password : ")
    while (re_pw != password ):
        re_pw = input("Wrong. Please rewrite your password again : ")
    name = input("Enter your name : ")
    DOB = input("Enter your DOB( YYYY-MM-DD) : ")
    sex = int( input("Enter your sex( 0 for MALE, 1 for FEMALE)") )
    while (sex != 1) and (sex != 0):
        sex = int( input("Wrong input. Please enter again"))
    check_address = False
    while (check_address != True):
        print("Enter you address(province from 1 to 63)\nPress Ctrl+P to see your province code")
        prov = input("Your address code(1-63): ")
        #if(strlen(prov)
     
        province_model = ProvinceModel()
        for i in range(province_model.num() ):
            print("{0} : {1}".format(i+1, province_model.convert_to_name(i)))

def signin():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break
    authen = UserAuthen(username,password)
    if authen.checkAuthen():
        userModel = authen.getUserInfo()
        userManager = UserManager(userModel)
        afterLogin(userManager)
    else:
        print("Invalid username or password")

def showMes(user_manager):
    values = user_manager.showMes()
    i = 0
    for value in values:
        i+=1
        print("{0}.".format(1))
        print("\tsender : {0}".format(value[1]))
        print("\treceiver : {0}".format(value[2]))
        print("\tcontent : {0}".format(value[3]))
        print("\ttime : {0}".format(value[4]))
        print("")


def showDetailMes(user_manager):
    values = user_manager.showFriendList()
    print("Your friendlist: ")
    i = 0
    for value in values:
        i+=1
        print("\t{0}. {1}".format(i,value[0]))
    index = int(input("Enter index of person you chat with: "))
    person = values[index-1][0]
    chat_history = user_manager.getChatHistory(person)
    for chat in chat_history:
        if (chat[0] == person):
            print("{0}".format(chat[2]))
        else :
            print("\t\t\t{0}".format(chat[2]))
    return 0


def sendMes(user_manager):
    print("We offer you 2 ways:")
    print(" 1. Enter reciever username : Press 1")
    print(" 2. Enter Ctr+L then choose receiver by number of index")
    inp = input("Enter your choice: ").split(' ')[0]
    init = ord(inp[0])
    while switch(init):
        if case(49):
            receiver = input("To: ...")
            content = input("Content: ")
            user_manager.sendMes(receiver,content)
            break
        if case(12):
            values = user_manager.showFriendList()
            if (values == None):
                print("You haven't had any friends")
            else:
                i = 0
                print("You friendlist: ")
                for value in values:
                    i += 1
                    print(" {0}. : {1}".format( i, value[0]) )
                inp = int(input("Enter friend index number: "))
                content = input("Content: ")
                receiver = values[inp-1][0]
                res = user_manager.sendMes(receiver,content)
                if res == 1:
                    print("SENT")
                elif res == 0:
                    print("ERROR: You blocked user with username = {0}".format(receiver))
                elif res == 2:
                    print("ERROR: user with username = '{0}' does not exist".format(receiver))
            break
        print("Wrong syntax. Please try again")
        break


def addFriend(user_manager):
    users = user_manager.getAllUsers()
    print("All users: ")
    i = 0
    for user in users:
        i+=1
        print("\t{0}. {1}".value[1])
    inp = int(input("Enter person index number u want to add friend: "))
    value = user_manager.addFriend(users[i-1][1])
    if value == 0 : print("ERROR : you blocked him/her")
    elif value == 2 : print("You are already friend")
    elif value == 1 : print("Added friend successfully")


def showFriendList(user_manager):
    values = user_manager.showFriendList()
    for i in range(len(values)):
        print("{0}. {1}".format(i+1,values[i][0]))


def showFriendByAddr(user_manager):
    values = user_manager.groupByCity()
    province_model = ProvinceModel()
    check = ""
    count = 0
    for value in values:
        if (check != value[0]):
            print(" {0}".format(province_model.convert_to_name(value[1])))
            count = 0
        count +=1
        print("{0}. {1}".format(count,value[1]))


def block(user_manager):
    users = user_manager.getAllUsers()
    print("All users: ")
    i = 0
    for user in users:
        i+=1
        print("\t{0}. {1}".value[1])
    inp = int(input("Enter person index number u want to block: "))
    
    check = False
    res = user_manager.isFriend()
    if res == 1:
        print("You are friend. Are you sure you want to block him/her? (Enter Y/N)")
        check = True
    if not(check):
        res = user_manager.isBlocked()
        if res == 1: 
            print("Blocked already.")
            check = True
    if not(check):
        print("Are you sure you want to block him/her? (Enter Y/N)")

    inp = input("Your choice: ").split(" ")[0]
    choice = inp[0]
    while switch(choice):
        if case ('Y','y'):
            user_manager.block(users[i-1][1]) 
        if case ('N','n'):
            break;
        print("Wrong syntax. Please try again")
        break
    
    

def afterLogin(userManager):
    check = 1
    while (check):
        print("MENU\n")
        print("1. Send Messages ")
        print("2. Message")
        print("3. View Detail Message")
        print("4. Add friends")
        print("5. Show friend list")
        print("6. Block")
        print("7. Log out")
        print("Enter Ctr+l to display friendlist")
        print("Enter ctr+S to list friendList by address and username (in order asc)")
        print("Enter Ctr+B to go back")
        inp = input("Enter a number (1-7): ").split(" ")[0]
        ch = ord(inp[0])

        while switch(ch):
            if case(49): 
                sendMes(userManager)
                break
            if case(50):
                showMes(userManager)
                break
            if case(51):
                showDetailMes(userManager)
                break
            if case(52):
                addFriend(userManager)
                break
            if case(53,12):
                showFriendList(userManager)
                break
            if case(54):
                block(userManager)
                break
            if case(55,2):
                check = 0
                break
            if case(19):
                showFriendByAddr(userManager)
                break

            print("Wrong syntax. Please try again")
            break
            
                


def main():
    check = 1
    while(check):
        print("CHAT APP")
        print("1.SIGN IN")
        print("2.SIGN UP")
        print("3. Exit application")
        init = int(input("Enter a number (1-3): "))
        while switch(init):
            if case(1): 
                signin()
                break
            if case(2): 
                signup()
                break
            if case(3):
                print("GOOD BYE")
                check = 0
                break
            print("Wrong syntax. Please try again")
            break

if __name__ == '__main__':
    main()