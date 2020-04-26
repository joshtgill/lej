class IOService:

    def __init__(self, calcService):
        self.calcService = calcService


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


    def displayProfile(self, undergrad):
        print('{} {} - {}\n'.format(undergrad.firstName, undergrad.lastName, undergrad.email))

        print('Transferred courses: {}'.format(len(undergrad.transferredCourses)))
        print('Completed courses: {}'.format(self.calcService.countUndergradCourses(undergrad.pastTerms)))
        print('Completed units: {}'.format(self.calcService.countUndergradUnits(undergrad.pastTerms)))
        print('Cumulative GPA: {}'.format(self.calcService.calcUndergradGpa(undergrad.pastTerms)))


    def displayTransferredCourses(self, undergrad):
        table = []
        for transferredCourse in undergrad.transferredCourses:
            table.append(['{} {}'.format(transferredCourse.subject, transferredCourse.number), transferredCourse.title, transferredCourse.units])

        self.printTable(['Course', 'Title', 'Units'], table, 10)


    def displayPastTerms(self, undergrad):
        table = []
        for pastTerm in undergrad.pastTerms:
            for pastCourse in pastTerm.courses:
                table.append(['{} {}'.format(pastCourse.subject, pastCourse.number), pastCourse.title, pastCourse.units, pastCourse.letterGrade, pastTerm.getTitle()])

        self.printTable(['Course', 'Title', 'Units', 'Grade', 'Term'], table, 10)


    def printTable(self, header, table, spaces):
        # Cast all table elements to string
        for rowIndex in range(len(table)):
            for colIndex in range(len(table[rowIndex])):
                table[rowIndex][colIndex] = str(table[rowIndex][colIndex])

        # Find and store the longest element in each column
        maxColElementLengths = []
        for colIndex in range(len(header)):
            maxColElementLength = 0
            for row in table:
                maxColElementLength = len(row[colIndex]) if len(row[colIndex]) > maxColElementLength else maxColElementLength
            maxColElementLengths.append(maxColElementLength)

        # Print formatted header
        for colIndex in range(len(header)):
            print(header[colIndex], end=' ' * (maxColElementLengths[colIndex] - len(header[colIndex]) + spaces))
        print()

        # Print formatted data
        for row in table:
            colIndex = 0
            while colIndex < len(row):
                print(row[colIndex], end=' ' * (maxColElementLengths[colIndex] - len(row[colIndex]) + spaces))
                colIndex += 1
            print()
