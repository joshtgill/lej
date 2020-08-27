import sys
from common.file_interface import FileInterface
from common.data_interface import DataInterface
from common.data_wrapper import DataWrapper
from common.io_interface import IOInterface
from account.account_manager import AccountManager
from academics.calculator import Calculator


class Lej:

    def __init__(self):
        self.fileInterface = FileInterface()
        self.dataInterface = DataInterface(self.fileInterface)
        self.dataWrapper = DataWrapper(self.dataInterface)
        self.ioInterface = IOInterface()
        self.accountManager = AccountManager(self.dataInterface, self.dataWrapper, self.ioInterface)
        self.calculator = Calculator(self.dataInterface)
        self.navigation = [{'Create account': self.createAccount, 'Login': self.login, 'Exit': self.back},
                           {'View profile': self.viewProfile, 'View academic history': self.viewAcademicHistory, 'Back': self.back},
                           {'View transferred courses': self.viewTransferredCourses, 'View past terms': self.viewPastTerms, 'Back': self.back}]
        self.navigationIndex = 0


    def start(self):
        while True:
            menuOptions = list(self.navigation[self.navigationIndex].keys())
            menuActions = list(self.navigation[self.navigationIndex].values())

            # Get user selection and launch corresponding action
            userSelection = self.ioInterface.handleMenuInput('Select action', menuOptions)
            menuActions[userSelection - 1]()


    def createAccount(self):
        self.navigationIndex += 1 if self.accountManager.createAccount() else 0

        self.ioInterface.println(additionalNewLines=1)


    def login(self):
        self.navigationIndex += 1 if self.accountManager.login() else 0

        self.ioInterface.println(additionalNewLines=1)


    def viewProfile(self):
        self.ioInterface.println('Name: {} {}'.format(self.accountManager.user.firstName, self.accountManager.user.lastName))
        self.ioInterface.println('Email: {}'.format(self.accountManager.user.email))
        self.ioInterface.println('ID: {}'.format(self.accountManager.user.id))
        majorTitles = [self.dataWrapper.getMajorTitleFromUuid(majorUuid) for majorUuid in self.accountManager.user.majors]
        self.ioInterface.println('Major(s): {}'.format(', '.join(majorTitles)))
        minorTitles = [self.dataWrapper.getMinorTitleFromUuid(minorUuid) for minorUuid in self.accountManager.user.minors]
        self.ioInterface.println('Minor(s): {}'.format(', '.join(minorTitles)))
        cumulativeGpa = self.calculator.calculateCumulativeGpa(self.accountManager.user)
        self.ioInterface.println('Cumulative GPA: {}'.format(round(cumulativeGpa, 3)))

        self.ioInterface.println(additionalNewLines=1)


    def viewAcademicHistory(self):
        self.navigationIndex += 1


    def viewTransferredCourses(self):
        for transferredCourse in self.accountManager.user.transferredCourses:
            self.ioInterface.println('{}{} {} ({})'.format(transferredCourse.subject, transferredCourse.number, transferredCourse.title, transferredCourse.units))

        self.ioInterface.println(additionalNewLines=1)


    def viewPastTerms(self):
        for pastTerm in self.accountManager.user.pastTerms:
            self.ioInterface.println('{} ({}): {}'.format(pastTerm.getTitle(),
                                                          self.calculator.countTermUnits(pastTerm),
                                                          round(self.calculator.calculateTermGpa(pastTerm), 3)))
            for course in pastTerm.courses:
                self.ioInterface.println('{}{} {} ({}): {}'.format(course.subject, course.number, course.title, course.units, course.letterGrade))
            self.ioInterface.println()

        self.ioInterface.println(additionalNewLines=1)


    def back(self):
        if self.navigationIndex == 0:
            sys.exit()

        self.navigationIndex -= 1 # TODO: Will not always work
