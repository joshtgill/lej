from managers.data_manager import DataManager
from managers.account_manager import AccountManager
from managers.io_manager import IOManager
from structures.user import User
import sys


class Lej:

    def __init__(self):
        # Various managers to be used and injected throughout application.
        self.localDb = DataManager('data/local_db.json')
        self.lejDb = DataManager('data/lej_db.json')
        self.ioManager = IOManager()
        self.accountManager = AccountManager(self.localDb, self.lejDb, self.ioManager)

        # Define the application's navigation, where each element represents a navigation grouping.
        self.navDirectory = [{'Create Account': self.createAccount, 'Login': self.login, 'Exit': self.stop},
                              {'View profile': self.viewProfile, 'View courses': self.viewCourses, 'Logout': self.logout, 'Exit': self.stop},
                              {'View transferred courses': self.viewTransferredCourses, 'View past courses': self.viewPastCourses, 'Back': self.back}]
        self.navIndex = 1 if self.accountManager.autoLogin() else 0


    def start(self):
        # Display active navigation group and handle the selection
        while True:
            userSelection = self.ioManager.handleMenuInput(*self.navDirectory[self.navIndex].keys())
            self.navIndex = list(self.navDirectory[self.navIndex].values())[userSelection - 1]()

            self.ioManager.println()


    def createAccount(self):
        result = self.accountManager.createAccount()
        if result:
            self.ioManager.println()

            return self.navIndex + 1

        return self.navIndex


    def login(self):
        result = self.accountManager.login()
        if result:
            self.ioManager.println()

            return self.navIndex + 1

        return self.navIndex


    def viewProfile(self):
        self.ioManager.displayProfile(self.accountManager.user)

        return self.navIndex


    def viewCourses(self):
        return self.navIndex + 1


    def viewTransferredCourses(self):
        self.ioManager.displayTransferredCourses(self.accountManager.user)

        return self.navIndex


    def viewPastCourses(self):
        self.ioManager.displayPastCourses(self.accountManager.user)

        return self.navIndex


    def logout(self):
        self.accountManager.logout()

        return self.navIndex - 1


    def back(self):
        return self.navIndex - 1


    def stop(self):
        sys.exit()
