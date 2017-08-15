class User:
    def __init__(self, n):
        self.name = n
        self.friend_list = []
    def addFriend(self, friend):
        self.friend_list.append(friend)
    def getName(self):
        return self.name
    def getFriends(self):
        emptyString = ""
        for count in range(len(self.friend_list)):
            if count == 0:
                emptyString = emptyString  + str(self.friend_list[count])
            else:
                emptyString = emptyString  + ", " + str(self.friend_list[count])
        return emptyString
    def __str__(self):
        nameInfo = "Name: " + str(self.name)
        friendInfo = "Friends: " + str(self.getFriends())
        return nameInfo + "  " + friendInfo


#print(user1.__str__())

class Network:
    def __init__(self):
        self.user_list = []
    #    self.usernames_list = [user1, user2]
    def getUser(self, username):
        for user in self.user_list:
            if username == user.getName():
                return user
            else:
                return None

    def addUser(self, name):
        for user in self.user_list:
            if user.getName() == name:
                return False
            else:
                person = User(name)
                self.user_list.append(person)
                return True

    def __str__(self):
        emptyString2 = ""
        usernameInfo = ""
        friendslistInfo = ""
        for user in self.user_list:
            usernameInfo = "User: " + str(user.getName())
            friendslistInfo = "Friends: " + str(user.getFriends())
            emptyString2 = emptyString2 + usernameInfo + "\t" + friendslistInfo + "\n"
        return emptyString2

"""user1 = User("bob")
user1.addFriend("frank")
user1.addFriend("will")

user2 = User("jeff")
user2.addFriend("jake")
user2.addFriend("ken")"""

networker = Network()
networker.addUser("bob")
#networker.addUser("jeff")
print(networker)
#print(networker.getUser(user2))
