from academics.course.course import Course


class Term:

    def __init__(self):
        self.semester = ''
        self.year = 0


    def getTitle(self):
        return '{} {}'.format(self.semester, self.year)


    def serialize(self):
        return {'semester': self.semester, 'year': self.year}


    def deserialize(self, data):
        self.semester = data.get('semester')
        self.year = int(data.get('year'))
