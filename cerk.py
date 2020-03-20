from data_manager import DataManager
from io_manager import IOManager
from user import User
import sys


class Cerk:

    def __init__(self):
        self.dataManager = DataManager('data.json')
        self.users = self.dataManager.loadUsers()
        self.ioManager = IOManager()

        self.activeNav = [{'Create Account': self.createAccount, 'Login': self.login, 'Exit': self.stop},{'Filler': self.filler}]
        self.activeNavIndex = 0

    def start(self):
        if self.users == []:
            self.createAccount()
            print()

        while True:
            userAction = self.ioManager.handleMenuInput(*self.activeNav[self.activeNavIndex].keys())

            self.activeNavIndex = list(self.activeNav[self.activeNavIndex].values())[userAction - 1]()

            print()


    def createAccount(self):
        userEmail, userPassword, userFirstName, userLastName = self.ioManager.gatherCreateAccountInfo()

        for user in self.users:
            if user.email == userEmail:
                this.ioManager.displayErrorMessage('Email already in use')
                return

        newUser = User(userEmail, userPassword, userFirstName, userLastName)
        self.users.append(newUser)
        self.dataManager.saveUsers(self.users)

        return self.activeNavIndex


    def login(self):
        userEmail = self.ioManager.gatherEmail()
        foundUser = -1
        for user in self.users:
            if user.email == userEmail:
                foundUser = user
                break
        if foundUser == -1:
            self.ioManager.displayErrorMessage('Could not find account associated with provided email')
            return False

        userPassword = self.ioManager.gatherPassword()
        if foundUser.password == userPassword:
            return 1
        else:
            self.ioManager.displayErrorMessage('Password incorrect for provided email')
            return self.activeNavIndex


    def filler(self):
        print('Replace me')

        return self.activeNavIndex


    def stop(self):
        sys.exit()