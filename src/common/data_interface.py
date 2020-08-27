import json


class DataInterface:

    def __init__(self, fileInterface):
        self.fileInterface = fileInterface
        self.dataDirectory = {'USERS': 'data/users.json', 'MAJORS': 'data/majors.json', 'MINORS': 'data/minors.json'} # name: path


    def sett(self, dataName, path, value):
        # Prepare the data for iteration
        data = self.loadData(dataName)
        pathList = self.pathToList(path)
        lastKey = pathList.pop()

        # Iterate over data
        dataRunner = data
        for key in pathList:
            if key not in dataRunner:
                dataRunner.update({key: {}})
            dataRunner = dataRunner.get(key)

        # If value is None then delete the existing key
        if value:
            dataRunner.update({lastKey: value})
        else:
            value = dataRunner.pop(lastKey)

        self.saveData(dataName, data)

        return value


    def get(self, dataName, path, defaultData=None):
        # Prepare data for iteration
        data = self.loadData(dataName)
        pathList = self.pathToList(path)

        # Iterate over data
        try:
            dataRunner = data
            for key in pathList:
                if '[' in key:
                    keyIndex = int(key[key.index('[') + 1 : key.index(']')])
                    key = key[0: key.index('[')]
                    if key:
                        dataRunner = dataRunner.get(key)[keyIndex]
                    else:
                        dataRunner = dataRunner[keyIndex]
                else:
                    dataRunner = dataRunner.get(key)
        except AttributeError:
            return defaultData

        return dataRunner if dataRunner != None else defaultData


    def loadData(self, name):
        dataPath = self.dataDirectory.get(name)

        return json.loads(self.fileInterface.read(dataPath, '{}'))


    def saveData(self, name, data):
        dataPath = self.dataDirectory.get(name)
        self.fileInterface.write(dataPath, json.dumps(data))


    def pathToList(self, path):
        if path == '':
            return []

        return path.strip().strip('/').split('/')
