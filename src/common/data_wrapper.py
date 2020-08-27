class DataWrapper:

    def __init__(self, dataInterface):
        self.dataInterface = dataInterface


    def getUserUuidFromEmail(self, email):
        for uuid, userData in self.dataInterface.get('USERS', 'users', {}).items():
            if userData.get('email') == email:
                return uuid

        return None


    def getAccountTypeFromUuid(self, uuid):
        for dataUuid, userData, in self.dataInterface.get('USERS', 'users', {}).items():
            if dataUuid == uuid:
                return userData.get('type')

        return None


    def getUserDataFromUuid(self, uuid):
        return self.dataInterface.get('USERS', 'users/{}'.format(uuid), {})


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
