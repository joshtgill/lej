import json
from user import User


class DataManager:

    def __init__(self, dataFileName):
        self.dataFileName = dataFileName


    def saveUsers(self, users):
        with open(self.dataFileName, 'w+') as dataFile:
            json.dump(self.serializeUsers(users), dataFile)


    def serializeUsers(self, users):
        usersData = []
        for user in users:
            userData = {}
            for userClassMember in self.retrieveClassMembers(user):
                execStr = 'userData["{}"] = user.{}'.format(userClassMember, userClassMember)
                exec(execStr)
            usersData.append(userData)

        return usersData


    def loadUsers(self):
        try:
            with open(self.dataFileName, 'r') as dataFile:
                return self.deserializeUsersData(json.loads(dataFile.read()))
        except FileNotFoundError:
            return []


    def deserializeUsersData(self, usersData):
        users = []
        for userData in usersData:
            user = User()
            for userClassMember in self.retrieveClassMembers(User()):
                execStr = 'user.{} = userData["{}"]'.format(userClassMember, userClassMember)
                exec(execStr)
            users.append(user)

        return users


    def retrieveClassMembers(self, obj):
        classMembers = []
        for attribute in dir(obj):
            if not attribute.startswith('__') and not callable(getattr(obj, attribute)):
                classMembers.append(attribute)

        return classMembers
