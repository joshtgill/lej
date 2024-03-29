import uuid
from account.user import User
from account.adviser import Adviser
from account.undergrad import Undergrad


class AccountManager:

    def __init__(self, dataInterface, dataWrapper, ioInterface):
        self.dataInterface = dataInterface
        self.dataWrapper = dataWrapper
        self.ioInterface = ioInterface
        self.user = None


    def createAccount(self):
        # Retrieve general account info
        firstName = self.ioInterface.getInput('Enter first name: ')
        lastName = self.ioInterface.getInput('Enter last name: ')
        email = self.ioInterface.getInput('Enter email: ')

        # Determine account type
        accountType = self.ioInterface.handleMenuInput('Select account type', ['Admin', 'Adviser', 'Undergrad'])
        if accountType == 1: # Admin
            self.user = User(uuid.uuid4(), firstName, lastName, email, accountType)
        elif accountType == 2: # Adviser
            # Retrieve undergrad(s)
            selectedUndergradUuids = self.selectionHelper(self.dataWrapper.getAllUndergradNames, 'Select undergrad(s)', self.dataWrapper.getUndergradUuidFromName)

            self.user = Adviser(uuid.uuid4(), firstName, lastName, email, accountType, selectedUndergradUuids)
        elif accountType == 3: # Undergrad
            # Retrieve student ID, major(s), and minor(s)
            idd = self.ioInterface.getInput('Enter ID: ')
            selectedMajorUuids = self.selectionHelper(self.dataWrapper.getAllMajorTitles, 'Select major(s)', self.dataWrapper.getMajorUuidFromTitle)
            selectedMinorUuids = self.selectionHelper(self.dataWrapper.getAllMinorTitles, 'Select minor(s)', self.dataWrapper.getMinorUuidFromTitle)

            self.user = Undergrad(uuid.uuid4(), idd, firstName, lastName, email, accountType, selectedMajorUuids, selectedMinorUuids)

        self.dataInterface.sett('USERS', '{}/{}'.format(accountType, self.user.uuid), self.user.serialize())
        self.ioInterface.println()
        self.ioInterface.println('Account created.')

        return True


    def selectionHelper(self, getOptionsFunction, menuInputLabel, getValueFunction, noneOption=True):
        # Get the options, adding 'None' if specified
        options = getOptionsFunction()
        if noneOption:
            options.append('None')

        # Get the numeric selections from user
        selections = self.ioInterface.handleMenuInput(menuInputLabel, options, True)

        # Based on selections, get the desired values
        selectedValues = []
        if not noneOption or len(options) not in selections:
            selectedValues = [getValueFunction(options[selection - 1]) for selection in selections]

        return selectedValues


    def login(self):
        inputEmail = self.ioInterface.getInput('Enter email: ')

        uuid = self.dataWrapper.getUserUuidFromEmail(inputEmail)
        if not uuid:
            return False

        accountType = self.dataWrapper.getAccountTypeFromUuid(uuid)
        if accountType == 1:
            self.user = User()
        elif accountType == 2:
            self.user = Adviser()
        elif accountType == 3:
            self.user = Undergrad()

        self.user.deserialize(uuid, self.dataWrapper.getUserDataFromUuid(uuid))

        return True
