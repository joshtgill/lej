import json
from user import User
from io_manager import IOManager


class DataManager:

    def __init__(self, dataFileName):
        self.dataFileName = dataFileName

        self.ioManager = IOManager()
        self.data = self.loadData()


    def saveData(self):
        with open(self.dataFileName, 'w+') as dataFile:
            json.dump(self.data, dataFile)


    def loadData(self):
        data = {}
        try:
            with open(self.dataFileName, 'r') as dataFile:
                data = json.loads(dataFile.read())
        except FileNotFoundError:
            pass

        return data


    def appendData(self, path, data):
        self.data[path].append(data.serialize())
        self.saveData()


    def getObjectList(self, path, objectType):
        objectList = []
        for data in self.data[path]:
            objectt = objectType()
            objectt.deserialize(data)
            objectList.append(objectt)

        return objectList
