from data_service import DataService
from account_service import AccountService
from calc_service import CalcService
from io_service import IOService
from structures.accounts.undergrad import Undergrad
import sys


class Lej:

    def __init__(self):
        # Various services to be used and injected throughout application.
        self.localDb = DataService('data/local_db.json')
        self.lejDb = DataService('data/lej_db.json')
        self.calcService = CalcService()
        self.ioService = IOService(self.calcService)
        self.accountService = AccountService(self.localDb, self.lejDb, self.ioService)


        # Define the application's navigation, where each element represents a navigation grouping.
        self.navDirectory = [{'Create Account': self.createAccount, 'Login': self.login, 'Exit': self.stop},
                              {'View profile': self.viewProfile, 'View academic history': self.viewAcademicHistory, 'Logout': self.logout, 'Exit': self.stop},
                              {'View transferred courses': self.viewTransferredCourses, 'View past terms': self.viewPastTerms, 'Back': self.back}]
        self.navIndex = 1 if self.accountService.autoLogin() else 0


    def start(self):
        # Display active navigation group and handle the selection
        while True:
            userSelection = self.ioService.handleMenuInput(*self.navDirectory[self.navIndex].keys())
            self.navIndex = list(self.navDirectory[self.navIndex].values())[userSelection - 1]()

            self.ioService.println()


    def createAccount(self):
        result = self.accountService.createAccount()
        if result:
            self.ioService.println()

            return self.navIndex + 1

        return self.navIndex


    def login(self):
        result = self.accountService.login()
        if result:
            self.ioService.println()

            return self.navIndex + 1

        return self.navIndex


    def viewProfile(self):
        self.ioService.displayProfile(self.accountService.undergrad)

        return self.navIndex


    def viewAcademicHistory(self):
        return self.navIndex + 1


    def viewTransferredCourses(self):
        self.ioService.displayTransferredCourses(self.accountService.undergrad)

        return self.navIndex


    def viewPastTerms(self):
        self.ioService.displayPastTerms(self.accountService.undergrad)

        return self.navIndex


    def logout(self):
        self.accountService.logout()

        return self.navIndex - 1


    def back(self):
        return self.navIndex - 1


    def stop(self):
        sys.exit()
