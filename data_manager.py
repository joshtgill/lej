import json
from user import User
from io_manager import IOManager


class DataManager:

    def __init__(self, dataFileName):
        self.dataFileName = dataFileName
        self.ioManager = IOManager()
        self.data = self.load()


    def save(self):
        with open(self.dataFileName, 'w+') as dataFile:
            json.dump(self.data, dataFile)


    def load(self):
        data = {}
        try:
            with open(self.dataFileName, 'r') as dataFile:
                data = json.loads(dataFile.read())
        except FileNotFoundError:
            pass

        return data


    def update(self, path, value, append = False):
        # Make list from path string
        pathList = path.strip().strip('/').split('/')

        # Get key from last item of path list
        key = pathList.pop()

        # Traverse data down path, creating keys if necessary
        dataRunner = self.data
        for pathItem in pathList:
            if pathItem not in dataRunner:
                dataRunner.update({pathItem: {}})
            dataRunner = dataRunner.get(pathItem)

        # Attempt to serialize value
        try:
            value = value.serialize()
        except AttributeError:
            pass

        # Append or set value depending on type
        if append:
            if dataRunner == {}:
                dataRunner.update({key: []})
            dataRunner.get(key).append(value)
        else:
            dataRunner.update({key: value})

        # Save updated data
        self.save()


    def query(self, path, Obj = None):
        # Make list from path string
        pathList = path.strip().strip('/').split('/')

        # Traverse data down path
        dataRunner = self.data
        for pathItem in pathList:
            dataRunner = dataRunner.get(pathItem)

        # If None, the assume attempting to append to empty list
        if dataRunner == None:
            return []

        # Build found data
        if isinstance(dataRunner, list):
            itemList = []
            for item in dataRunner:
                if Obj is not None:
                    obj = Obj()
                    obj.deserialize(item)
                    itemList.append(obj)
                else:
                    itemList.append(item)

            return itemList
        else:
            if Obj is not None:
                obj = Obj()
                obj.deserialize(dataRunner)

                return obj
            else:
                return dataRunner
