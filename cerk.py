from data_manager import DataManager
from io_manager import IOManager
from user import User
import sys


class Cerk:

    def __init__(self):
        self.dataManager = DataManager('data.json')
        self.ioManager = IOManager()

        self.navigation = [{'Create Account': self.createAccount, 'Login': self.login, 'Exit': self.stop},
                           {'Logout': self.logout}]
        self.navigationIndex = 0


    def start(self):
        while True:
            userAction = self.ioManager.handleMenuInput(*self.navigation[self.navigationIndex].keys())
            self.navigationIndex = list(self.navigation[self.navigationIndex].values())[userAction - 1]()

            print()


    def createAccount(self):
        userEmail = self.ioManager.gatherEmail()
        for user in self.dataManager.getObjectList('users', User):
            if user.email == userEmail:
                self.ioManager.displayErrorMessage('Email already in use.')
                return self.navigationIndex

        newUser = User(userEmail, self.ioManager.gatherPassword(), self.ioManager.gatherFirstName(), self.ioManager.gatherLastName())
        self.dataManager.appendData('users', newUser)

        return self.navigationIndex


    def login(self):
        userEmail = self.ioManager.gatherEmail()
        foundUser = None
        for user in self.dataManager.getObjectList('users', User):
            if user.email == userEmail:
                foundUser = user
                break
        if foundUser == None:
            self.ioManager.displayErrorMessage('Could not find account associated with provided email.')
            return self.navigationIndex

        userPassword = self.ioManager.gatherPassword()
        if foundUser.password == userPassword:
            return self.navigationIndex + 1
        else:
            self.ioManager.displayErrorMessage('Password incorrect for provided email.')
            return self.navigationIndex


    def logout(self):
        return self.navigationIndex - 1


    def stop(self):
        sys.exit()