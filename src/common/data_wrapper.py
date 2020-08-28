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
        for accountTypeKey in self.dataInterface.get('USERS', '', {}):
            for dataUuid, userData, in self.dataInterface.get('USERS', accountTypeKey, {}).items():
                if dataUuid == uuid:
                    return userData.get('type')

        return None


    # TODO: Optimize FromUuid methods
    def getUserDataFromUuid(self, uuid):
        for accountTypeKey in self.dataInterface.get('USERS', '', {}):
            for dataUuid, userData in self.dataInterface.get('USERS', accountTypeKey, {}).items():
                if dataUuid == uuid:
                    return userData

        return None


    def getAllUndergradNames(self):
        return ['{} {}'.format(userData.get('firstName'), userData.get('lastName'))
                               for _, userData in self.dataInterface.get('USERS', '3/', {}).items()]


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
        for dataUuid, majorData in self.dataInterface.get('MAJORS', '', {}).items():
            if dataUuid == uuid:
                return majorData.get('title')

        return None


    def getMajorUuidFromTitle(self, title):
        for dataUuid, majorData in self.dataInterface.get('MAJORS', '', {}).items():
            if majorData.get('title') == title:
                return dataUuid

        return None


    def getAllMinorTitles(self):
        return [minorData.get('title') for _, minorData in self.dataInterface.get('MINORS', '', {}).items()]


    def getMinorTitleFromUuid(self, uuid):
        for dataUuid, minorData in self.dataInterface.get('MINORS', '', {}).items():
            if dataUuid == uuid:
                return minorData.get('title')

        return None


    def getMinorUuidFromTitle(self, title):
        for dataUuid, minorData in self.dataInterface.get('MINORS', '', {}).items():
            if minorData.get('title') == title:
                return dataUuid

        return None


    def getValueFromLetterGrade(self, letterGrade):
        return self.dataInterface.get('SETTINGS', 'letterGradeValueDirectory').get(letterGrade)
