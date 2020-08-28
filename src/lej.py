import sys
from common.file_interface import FileInterface
from common.data_interface import DataInterface
from common.data_wrapper import DataWrapper
from common.io_interface import IOInterface
from account.account_manager import AccountManager
from academics.calculator import Calculator
import uuid


class Lej:

    def __init__(self):
        self.fileInterface = FileInterface()
        self.dataInterface = DataInterface(self.fileInterface)
        self.dataWrapper = DataWrapper(self.dataInterface)
        self.ioInterface = IOInterface()
        self.accountManager = AccountManager(self.dataInterface, self.dataWrapper, self.ioInterface)
        self.calculator = Calculator(self.dataInterface, self.dataWrapper)
        self.navigation = [{'Create account': self.createAccount, 'Login': self.login, 'Exit': self.back}]
        self.navigationIndex = 0


    def start(self):
        while True:
            menuOptions = list(self.navigation[self.navigationIndex].keys())
            menuActions = list(self.navigation[self.navigationIndex].values())

            # Get user selection and launch corresponding action
            userSelection = self.ioInterface.handleMenuInput('Select action', menuOptions)
            menuActions[userSelection - 1]()


    def createAccount(self):
        if self.accountManager.createAccount():
            self.updateNavigation()
            self.navigationIndex += 1

        self.ioInterface.println(additionalNewLines=1)


    def login(self):
        if self.accountManager.login():
            self.updateNavigation()
            self.navigationIndex += 1

        self.ioInterface.println(additionalNewLines=1)


    def updateNavigation(self):
        if self.accountManager.user.type == 1:
            self.navigation.extend([{'Create major': self.createMajor, 'Create minor': self.createMinor}])
        elif self.accountManager.user.type == 2:
            self.navigation.extend([{'View profile': self.viewAdviserProfile, 'Back': self.back}])
        elif self.accountManager.user.type == 3:
            self.navigation.extend([{'View profile': self.viewUndergradProfile, 'View academic history': self.viewAcademicHistory, 'Back': self.back},
                                    {'View transferred courses': self.viewTransferredCourses, 'View past terms': self.viewPastTerms, 'Back': self.back}])


    def createMajor(self):
        majorTitle = self.ioInterface.getInput('Enter major title: ')
        self.dataWrapper.createMajor(uuid.uuid4(), majorTitle)

        self.ioInterface.println('Major created.', additionalNewLines=2)


    def createMinor(self):
        minorTitle = self.ioInterface.getInput('Enter minor title: ')
        self.dataWrapper.createMinor(uuid.uuid4(), minorTitle)

        self.ioInterface.println('Minor created.', additionalNewLines=2)


    def viewAdviserProfile(self):
        self.ioInterface.println('Name: {} {}'.format(self.accountManager.user.firstName, self.accountManager.user.lastName))
        self.ioInterface.println('Email: {}'.format(self.accountManager.user.email))
        undergradNames = [self.dataWrapper.getUndergradNameFromUuid(undergradUuid) for undergradUuid in self.accountManager.user.undergrads]
        self.ioInterface.println('Undergrad(s): {}'.format(', '.join(undergradNames)))

        self.ioInterface.println(additionalNewLines=1)


    def viewUndergradProfile(self):
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

        self.ioInterface.println()


    def back(self):
        if self.navigationIndex == 0:
            sys.exit()
        elif self.navigationIndex == 1:
            self.navigation = [{'Create account': self.createAccount, 'Login': self.login, 'Exit': self.back}]

        self.navigationIndex -= 1 # TODO: Will not always work
