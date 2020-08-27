from academics.course.course import Course


class PastCourse(Course):

    def __init__(self):
        super().__init__()
        self.letterGrade = ''


    def serialize(self):
        return super().serialize().update({'letterGrade': self.letterGrade})


    def deserialize(self, data):
        super().deserialize(data)
        self.letterGrade = data.get('letterGrade')
