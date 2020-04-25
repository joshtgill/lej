from structures.accounts.undergrad import Undergrad


class AccountManager:

    def __init__(self, localDb, lejDb, ioManager):
        self.localDb = localDb
        self.lejDb = lejDb
        self.ioManager = ioManager

        self.undergrad = None


    def autoLogin(self):
        uuid = self.localDb.query('uuid')
        if uuid != []:
            self.undergrad = self.lejDb.query('users/{}'.format(uuid), Undergrad)

            return True

        return False


    def login(self):
        userEmail = self.ioManager.gatherInput('Enter email: ')
        foundUser = None
        # Verify email exists
        for uuid in self.lejDb.query('users'):
            undergrad = self.lejDb.query('users/{}'.format(uuid), Undergrad)
            if undergrad.email == userEmail:
                foundUuid = uuid
                foundUser = undergrad
                break
        if foundUser == None:
            self.ioManager.displayErrorMessage('Could not find account associated with provided email.')

            return False

        userPassword = self.ioManager.gatherInput('Enter password: ')
        # Verify password corresponds with email
        if foundUser.password != userPassword:
            self.ioManager.displayErrorMessage('Password incorrect for provided email.')

            return False

        # Locally save login
        self.localDb.update('uuid', str(foundUuid))

        self.undergrad = foundUser

        return True


    def createAccount(self):
        userEmail = self.ioManager.gatherInput('Enter email: ')
        # Verify email doesn't already exist
        for uuid in self.lejDb.query('users'):
            undergrad = self.lejDb.query('users/{}'.format(uuid), Undergrad)
            if undergrad.email == userEmail:
                self.ioManager.displayErrorMessage('Email already in use.')

                return False

        # Create new undergrad and write to db
        newUser = Undergrad(userEmail, self.ioManager.gatherInput('Enter password: '), self.ioManager.gatherInput('Enter first name: '), self.ioManager.gatherInput('Enter last name: '))
        self.lejDb.update('users/{}'.format(newUser.uuid), newUser)

        # Locally save login
        self.localDb.update('uuid', str(newUser.uuid))

        self.undergrad = newUser

        return True


    def logout(self):
        # Wipe saved login
        self.localDb.update('', {})

        return True
