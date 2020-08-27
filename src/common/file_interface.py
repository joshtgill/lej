import os


class FileInterface:

    def write(self, path, data, append=False):
        locationDirectories = path.strip().strip('/').split('/')[: - 1]

        locationStr = ''
        for directory in locationDirectories:
            locationStr += directory + '/'
            if not os.path.exists(locationStr):
                os.mkdir(locationStr)

        with open(path, 'a+' if append else 'w+') as filee:
            filee.write(data)


    def read(self, path, defaultData=None):
        try:
            with open(path, 'r') as filee:
                return filee.read()
        except Exception:
            return defaultData


    def wipe(self, path):
        try:
            with open(path, 'w') as filee:
                return
        except Exception:
            return
