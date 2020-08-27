import uuid
from account.undergrad import Undergrad


class AccountManager:

    def __init__(self, dataInterface, dataWrapper, ioInterface):
        self.dataInterface = dataInterface
        self.dataWrapper = dataWrapper
        self.ioInterface = ioInterface
        self.user = None


    def createAccount(self):
        # Retrieve general account info
        idd = self.ioInterface.getInput('Enter ID: ')
        firstName = self.ioInterface.getInput('Enter first name: ')
        lastName = self.ioInterface.getInput('Enter last name: ')
        email = self.ioInterface.getInput('Enter email: ')

        # Determine account type
        accountType = self.ioInterface.handleMenuInput('Select account type', ['Admin', 'Adviser', 'Undergrad'])
        if accountType == 3: # Undergraduate
            # Retrieve major(s)
            majorTitlesOptions = self.dataWrapper.getAllMajorTitles()
            majorTitlesOptions.append('None')
            majorSelections = self.ioInterface.handleMenuInput('Select major', majorTitlesOptions, True)
            selectedMajorUuids = []
            if len(majorTitlesOptions) not in majorSelections: # If 'None' was selected, keep selected majors empty
                selectedMajorUuids = [self.dataWrapper.getMajorUuidFromTitle(majorTitlesOptions[userSelection - 1]) for userSelection in majorSelections]

            # Retrieve minor(s)
            minorTitlesOptions = self.dataWrapper.getAllMinorTitles()
            minorTitlesOptions.append('None')
            minorSelections = self.ioInterface.handleMenuInput('Select minor', minorTitlesOptions, True)
            selectedMinorUuids = []
            if len(minorTitlesOptions) not in minorSelections: # If 'None' was selected, keep selected minors empty
                selectedMinorUuids = [self.dataWrapper.getMinorUuidFromTitle(minorTitlesOptions[userSelection - 1]) for userSelection in minorSelections]

            self.user = Undergrad(uuid.uuid4(), idd, firstName, lastName, email, accountType, selectedMajorUuids, selectedMinorUuids)

        # Set and notify
        self.dataInterface.sett('USERS', 'users/{}'.format(self.user.uuid), self.user.serialize())
        self.ioInterface.println('User created.')

        return True


    def login(self):
        inputEmail = self.ioInterface.getInput('Enter email: ')

        uuid = self.dataWrapper.getUserUuidFromEmail(inputEmail)
        if not uuid:
            return False

        accountType = self.dataWrapper.getAccountTypeFromUuid(uuid)
        if accountType == 3:
            self.user = Undergrad()

        self.user.deserialize(uuid, self.dataWrapper.getUserDataFromUuid(uuid))

        return True
