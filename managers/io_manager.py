class IOManager:

    def println(self, numLines=1):
        for line in range(numLines):
            print()


    def gatherInput(self, prompt):
        return input(prompt)


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


    def handleMenuInput(self, *options):
        print('Enter selection -')

        i = 1
        for option in options:
            print('({}) {}'.format(i, option), end = '     ')
            i += 1
        print()

        userSelection = self.handleNumberInput('Selection #', 1, len(options))
        print()

        return userSelection


    def displayErrorMessage(self, message):
        print('\nERROR: {}'.format(message))


    def displayProfile(self, user):
        print('Name: {} {}'.format(user.firstName, user.lastName))
        print('Email: {}'.format(user.email))
        print('Password: {}'.format(user.password))


    def displayTransferredCourses(self, user):
        for transferredCourse in user.transferredCourses:
            print('[{} {}] {} - units: {}'.format(transferredCourse.subject, transferredCourse.number,
                                                                transferredCourse.title, transferredCourse.units))


    def displayPastCourses(self, user):
        for pastTerm in user.pastTerms:
            print('{} -'.format(pastTerm.getTitle()))
            for pastCourse in pastTerm.courses:
                print('\t{} ({} {}) - units: {}, grade: {}'.format(pastCourse.title, pastCourse.subject, pastCourse.number,
                                                                pastCourse.units, pastCourse.letterGrade))
