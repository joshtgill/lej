from user import User


class AccountManager:

    def __init__(self, localDb, lejDb, ioManager):
        self.localDb = localDb
        self.lejDb = lejDb
        self.ioManager = ioManager

        self.user = None


    def autoLogin(self):
        uuid = self.localDb.query('uuid')
        if uuid != []:
            self.user = self.lejDb.query('users/{}'.format(uuid), User)

            return True

        return False


    def login(self):
        userEmail = self.ioManager.gatherInput('Enter email: ')
        foundUser = None
        # Verify email exists
        for uuid in self.lejDb.query('users'):
            user = self.lejDb.query('users/{}'.format(uuid), User)
            if user.email == userEmail:
                foundUuid = uuid
                foundUser = user
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

        self.user = foundUser

        return True


    def createAccount(self):
        userEmail = self.ioManager.gatherInput('Enter email: ')
        # Verify email doesn't already exist
        for uuid in self.lejDb.query('users'):
            user = self.lejDb.query('users/{}'.format(uuid), User)
            if user.email == userEmail:
                self.ioManager.displayErrorMessage('Email already in use.')

                return False

        # Create new user and write to db
        newUser = User(userEmail, self.ioManager.gatherInput('Enter password: '), self.ioManager.gatherInput('Enter first name: '), self.ioManager.gatherInput('Enter last name: '))
        self.lejDb.update('users/{}'.format(newUser.uuid), newUser)

        # Locally save login
        self.localDb.update('uuid', str(newUser.uuid))

        self.user = newUser

        return True


    def logout(self):
        # Wipe saved login
        self.localDb.update('', {})

        return True


    def viewProfile(self):
        self.ioManager.displayProfile(self.user)

        return True


