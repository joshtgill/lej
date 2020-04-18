from data_manager import DataManager
from io_manager import IOManager
from user import User
import sys


class Lej:

    def __init__(self):
        self.localDb = DataManager('local_data.json')
        self.lejDb = DataManager('lej_data.json')
        self.ioManager = IOManager()

        self.user = None
        self.menuDirectory = [{'Create Account': self.createAccount, 'Login': self.login, 'Exit': self.stop},
                              {'View profile': self.viewProfile, 'Logout': self.logout, 'Exit': self.stop}]
        self.menuIndex = self.tryAutoLogin()


    def tryAutoLogin(self):
        # If uuid exists, login with corresponding account
        uuid = self.localDb.query('uuid')
        if uuid != []:
            self.user = self.lejDb.query('users/{}'.format(uuid), User)

            return 1

        return 0


    def start(self):
        # Display active menu and handle the selection
        while True:
            userSelection = self.ioManager.handleMenuInput(*self.menuDirectory[self.menuIndex].keys())
            self.menuIndex = list(self.menuDirectory[self.menuIndex].values())[userSelection - 1]()

            print()


    def createAccount(self):
        # Retrieve email and verify it doesn't exist in db
        userEmail = self.ioManager.gatherEmail()
        for user in self.lejDb.query('users', User):
            if user.email == userEmail:
                self.ioManager.displayErrorMessage('Email already in use.')

                return self.menuIndex

        # Create new user and write to db
        newUser = User(userEmail, self.ioManager.gatherPassword(), self.ioManager.gatherFirstName(), self.ioManager.gatherLastName())
        self.lejDb.update('users/{}'.format(newUser.uuid), newUser)

        return self.menuIndex


    def login(self):
        # Retrieve email and verify if exists
        userEmail = self.ioManager.gatherEmail()
        foundUser = None
        for uuid in self.lejDb.query('users', None):
            user = self.lejDb.query('users/{}'.format(uuid), User)
            if user.email == userEmail:
                foundUser = user
                break
        if foundUser == None:
            self.ioManager.displayErrorMessage('Could not find account associated with provided email.')

            return self.menuIndex

        # Retrieve password and verify it matches with email
        userPassword = self.ioManager.gatherPassword()
        if foundUser.password != userPassword:
            self.ioManager.displayErrorMessage('Password incorrect for provided email.')

            return self.menuIndex

        # Update user and save login
        self.user = foundUser
        self.localDb.update('uuid', str(foundUser.uuid))

        return self.menuIndex + 1


    def viewProfile(self):
        # Display user data
        self.ioManager.displayUserProfile(self.user)

        return self.menuIndex


    def logout(self):
        # Wipe saved login
        self.localDb.data = {}
        self.localDb.save()

        return self.menuIndex - 1


    def stop(self):
        sys.exit()