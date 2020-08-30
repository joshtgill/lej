class DataWrapper:

    def __init__(self, dataInterface):
        self.dataInterface = dataInterface


    def getUserUuidFromEmail(self, email):
        for accountTypeKey in self.dataInterface.get('USERS', '', {}):
            for uuid, userData in self.dataInterface.get('USERS', accountTypeKey, {}).items():
                if userData.get('email') == email:
                    return uuid

        return None


    def getAccountTypeFromUuid(self, uuid):
        for accountType in self.dataInterface.get('USERS', '', {}):
            userData = self.dataInterface.get('USERS', '{}/{}/'.format(accountType, uuid), None)
            if userData:
                return userData.get('type')

        return None


    def getUserDataFromUuid(self, uuid):
        for accountType in self.dataInterface.get('USERS', '', {}):
            userData = self.dataInterface.get('USERS', '{}/{}/'.format(accountType, uuid), {})
            if userData:
                return userData

        return None


    def getAdviserNameFromUuid(self, uuid):
        adviserData = self.dataInterface.get('USERS', '2/{}'.format(uuid), {})

        return '{} {}'.format(adviserData.get('firstName'), adviserData.get('lastName'))


    def getAllUndergradNames(self):
        return ['{} {}'.format(undergradData.get('firstName'), undergradData.get('lastName'))
                               for _, undergradData in self.dataInterface.get('USERS', '3/', {}).items()]


    def getUndergradNameFromUuid(self, uuid):
        undergradData = self.dataInterface.get('USERS', '3/' + uuid)

        return '{} {}'.format(undergradData.get('firstName'), undergradData.get('lastName'))


    def getUndergradUuidFromName(self, name):
        for dataUuid, undergradData in self.dataInterface.get('USERS', '3/', {}).items():
            if '{} {}'.format(undergradData.get('firstName'), undergradData.get('lastName')) == name:
                return dataUuid

        return None


    def getAllMajorTitles(self):
        return [majorData.get('title') for _, majorData in self.dataInterface.get('MAJORS', '', {}).items()]


    def getMajorTitleFromUuid(self, uuid):
        majorData = self.dataInterface.get('MAJORS', uuid, None)

        return majorData.get('title')


    def getMajorUuidFromTitle(self, title):
        for dataUuid, majorData in self.dataInterface.get('MAJORS', '', {}).items():
            if majorData.get('title') == title:
                return dataUuid

        return None


    def createMajor(self, uuid, title):
        self.dataInterface.sett('MAJORS', '{}/title/'.format(uuid), title)


    def getAllMinorTitles(self):
        return [minorData.get('title') for _, minorData in self.dataInterface.get('MINORS', '', {}).items()]


    def getMinorTitleFromUuid(self, uuid):
        minorData = self.dataInterface.get('MINORS', '', {}).items()

        return minorData.get('title')


    def getMinorUuidFromTitle(self, title):
        for dataUuid, minorData in self.dataInterface.get('MINORS', '', {}).items():
            if minorData.get('title') == title:
                return dataUuid

        return None


    def createMinor(self, uuid, title):
        self.dataInterface.sett('MINORS', '{}/title/'.format(uuid), title)


    def getValueFromLetterGrade(self, letterGrade):
        return self.dataInterface.get('SETTINGS', 'letterGradeValueDirectory').get(letterGrade)
