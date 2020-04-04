from data_manager import DataManager
from io_manager import IOManager
from user import User
import sys


class Cerk:

    def __init__(self):
        self.localDb = DataManager('local_data.json')
        self.cerkDb = DataManager('cerk_data.json')
        self.ioManager = IOManager()
        self.user = None
        self.menuDirectory = [{'Create Account': self.createAccount, 'Login': self.login, 'Exit': self.stop},
                              {'Logout': self.logout}]
        self.menuIndex = 0

        self.menuIndex = self.tryAutoLogin()


    def start(self):
        # Display active menu and handle selection
        while True:
            userSelection = self.ioManager.handleMenuInput(*self.menuDirectory[self.menuIndex].keys())
            self.menuIndex = list(self.menuDirectory[self.menuIndex].values())[userSelection - 1]()

            print()


    def createAccount(self):
        userEmail = self.ioManager.gatherEmail()
        for user in self.cerkDb.query('users', User):
            if user.email == userEmail:
                self.ioManager.displayErrorMessage('Email already in use.')

                return self.menuIndex

        newUser = User(userEmail, self.ioManager.gatherPassword(), self.ioManager.gatherFirstName(), self.ioManager.gatherLastName())
        self.cerkDb.update('users/{}'.format(newUser.uuid), newUser)

        return self.menuIndex


    def login(self):
        userEmail = self.ioManager.gatherEmail()
        foundUser = None
        for uuid in self.cerkDb.query('users', None):
            user = self.cerkDb.query('users/{}'.format(uuid), User)
            if user.email == userEmail:
                foundUser = user
                break
        if foundUser == None:
            self.ioManager.displayErrorMessage('Could not find account associated with provided email.')

            return self.menuIndex

        userPassword = self.ioManager.gatherPassword()
        if foundUser.password != userPassword:
            self.ioManager.displayErrorMessage('Password incorrect for provided email.')

            return self.menuIndex

        self.user = foundUser
        self.localDb.update('uuid', str(foundUser.uuid))

        return self.menuIndex + 1


    def tryAutoLogin(self):
        uuid = self.localDb.query('uuid')
        if uuid == []:
            return self.menuIndex
        else:
            self.user = self.cerkDb.query('users/uuid', User)

            return self.menuIndex + 1


    def logout(self):
        self.localDb.data = {}
        self.localDb.save()

        return self.menuIndex - 1


    def stop(self):
        sys.exit()