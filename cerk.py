from data_manager import DataManager
from io_manager import IOManager
from user import User


class Cerk:

    def __init__(self):
        self.dataManager = DataManager('data.json')
        self.users = self.dataManager.loadUsers()
        self.ioManager = IOManager()


    def start(self):
        while True:
            userAction = self.ioManager.handleMenuInput('Enter Action', 'Action #', 'Create Account', 'Exit')

            if userAction == 1:
                self.createAccount()
            elif userAction == 2:
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
