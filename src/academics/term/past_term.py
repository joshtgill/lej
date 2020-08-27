from academics.term.term import Term
from academics.course.past_course import PastCourse


class PastTerm(Term):

    def __init__(self):
        super().__init__()
        self.courses = []


    def serialize(self):
        termData = super().serialize()
        coursesData = []
        for course in self.courses:
            coursesData.append(course.serialize())
        termData.update({'courses': coursesData})

        return termData


    def deserialize(self, data):
        super().deserialize(data)
        for courseData in data.get('courses'):
            course = PastCourse()
            course.deserialize(courseData)
            self.courses.append(course)
