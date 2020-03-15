class IOManager:

    def handleMenuInput(self, title, prompt, *options):
        print('{} -'.format(title))

        i = 1
        for option in options:
            print('({}) {}'.format(i, option), end = '\t')
            i += 1
        print()

        userAction = self.handleNumberInput(prompt, 1, len(options))

        print()

        return userAction


    def handleNumberInput(self, prompt, minNumber, maxNumber):
        while True:
            userInput = input('{}: '.format(prompt))
            try:
                userNumber = int(userInput)
            except ValueError:
                self.displayErrorMessage('Input must be a number')
                continue

            if userNumber > maxNumber or userNumber < minNumber:
                self.displayErrorMessage('Input must be between {}-{}'.format(minNumber, maxNumber))
            else:
                return userNumber


    def displayErrorMessage(self, message):
        print('ERROR: {}.'.format(message))


    def gatherCreateAccountInfo(self):
        userEmail = input('Enter email: ')
        userPassword = input('Enter password: ')
        userFirstName = input('Enter first name: ')
        userLastName = input('Enter last name: ')

        return userEmail, userPassword, userFirstName, userLastName


    def gatherEmail(self):
        return input('Enter email: ')


    def gatherPassword(self):
        return input('Enter password: ')
