class Course:

    def __init__(self):
        self.subject = ''
        self.number = 0
        self.title = ''
        self.credits = 0
        self.letterGrade = ''


    def deserialize(self, data):
        self.subject = data.get('subject')
        self.number = data.get('number')
        self.title = data.get('title')
        self.credits = data.get('credits')
        self.letterGrade = data.get('letterGrade')
