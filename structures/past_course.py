from structures.course import Course


class PastCourse(Course):

    def __init__(self):
        super().__init__()
        self.letterGrade = ''


    def serialize(self):
        courseData = super().serialize()
        courseData.update({'letterGrade': self.letterGrade})

        return courseData


    def deserialize(self, data):
        super().deserialize(data)
        self.letterGrade = data.get('letterGrade')
