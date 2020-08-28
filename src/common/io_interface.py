class IOInterface:

    def println(self, message='', end='\n', additionalNewLines=0):
        print(message, end=end)

        for i in range(additionalNewLines):
            print()


    def displayErrorMessage(self, message):
        print('ERROR: {}'.format(message))


    def getInput(self, prompt):
        return input(prompt)


    def getNumberInput(self, prompt, minNumber, maxNumber, multiple=False):
        while True:
            numbers = self.getInput(prompt).strip().split(' ')
            if not multiple and len(numbers) > 1:
                self.displayErrorMessage('Input must be a single number.')

            inputError = False
            for number in numbers:
                try:
                    number = int(number)
                except ValueError:
                    self.displayErrorMessage('Input(s) must be a number.')
                    inputError = True
                    break

                if number < minNumber or number > maxNumber:
                    self.displayErrorMessage('Input(s) must be in range {}-{}.'.format(minNumber, maxNumber))
                    inputError = True
                    break


            if not inputError:
                numbers = [int(n) for n in numbers]
                return numbers if multiple else numbers[0]


    def handleMenuInput(self, prompt, options, multiple=False):
        # Display menu input
        self.println('{} -'.format(prompt))
        i = 1
        for option in options:
            self.println('({}) {}'.format(i, option), '     ')
            i += 1
        self.println()

        # Get menu input
        userSelection = self.getNumberInput('Selection #: ', 1, len(options), multiple)

        return userSelection
