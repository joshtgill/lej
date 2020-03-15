from data_manager import DataManager
from io_manager import IOManager
from user import User


class Cerk:

    def __init__(self):
        self.dataManager = DataManager('data.json')
        self.users = self.dataManager.loadUsers()
        self.ioManager = IOManager()


    def start(self):
        if self.users == []:
            self.createAccount()
            print()

        while True:
            userAction = self.ioManager.handleMenuInput('Enter Action', 'Action #', 'Create Account', 'Login', 'Exit')

            if userAction == 1:
                self.createAccount()
            elif userAction == 2:
                self.login()
            elif userAction == 3:
                return

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
            return True
        else:
            self.ioManager.displayErrorMessage('Password incorrect for provided email')
            return False
