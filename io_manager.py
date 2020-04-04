class IOManager:

    def handleMenuInput(self, *options):
        print('Enter selection -')

        i = 1
        for option in options:
            print('({}) {}'.format(i, option), end = '\t')
            i += 1
        print()

        userSelection = self.handleNumberInput('Selection #', 1, len(options))
        print()

        return userSelection


    def handleNumberInput(self, prompt, minNumber, maxNumber):
        while True:
            userInput = input('{}: '.format(prompt))
            try:
                userNumber = int(userInput)
            except ValueError:
                self.displayErrorMessage('Input must be a number.')
                continue

            if userNumber > maxNumber or userNumber < minNumber:
                self.displayErrorMessage('Input must be between {}-{}.'.format(minNumber, maxNumber))
            else:
                return userNumber


    def displayErrorMessage(self, message):
        print('\nERROR: {}'.format(message))


    def displayUserProfile(self, user):
        print('Name: {} {}'.format(user.firstName, user.lastName))
        print('Email: {}'.format(user.email))
        print('Password: {}'.format(user.password))


    def gatherEmail(self):
        return input('Enter email: ')


    def gatherPassword(self):
        return input('Enter password: ')


    def gatherFirstName(self):
        return input('Enter first name: ')


    def gatherLastName(self):
        return input('Enter last name: ')