class Course:

    def __init__(self):
        self.subject = ''
        self.number = 0
        self.title = ''
        self.units = 0


    def serialize(self):
        return {'subject': self.subject, 'number': self.number, 'title': self.title, 'units': self.units}


    def deserialize(self, data):
        self.subject = data.get('subject')
        self.number = data.get('number')
        self.title = data.get('title')
        self.units = data.get('units')
