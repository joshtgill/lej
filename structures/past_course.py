from structures.course import Course


class PastCourse(Course):

    def __init__(self):
        self.letterGrade = ''


    def deserialize(self, data):
        super().deserialize(data)
        self.letterGrade = data.get('letterGrade')
