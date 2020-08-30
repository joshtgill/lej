from account.user import User
from academics.course.course import Course
from academics.term.past_term import PastTerm


class Undergrad(User):

    def __init__(self, uuid=None, idd='', firstName='', lastName='', email='', typee=-1, majors=[], minors=[]):
        super().__init__(uuid, firstName, lastName, email, typee)
        self.id = idd
        self.advisers = []
        self.majors = majors
        self.minors = minors
        self.transferredCourses = []
        self.pastTerms = []


    def serialize(self):
        data = super().serialize()

        data.update({'id': self.id})
        data.update({'advisers': self.advisers})
        data.update({'majors': self.majors})
        data.update({'minors': self.minors})

        return data


    def deserialize(self, uuid, data):
        super().deserialize(uuid, data)

        self.id = data.get('id')
        self.advisers = data.get('advisers')
        self.majors = data.get('majors')
        self.minors = data.get('minors')

        for transferredCourseData in data.get('transferredCourses'):
            transferredCourse = Course()
            transferredCourse.deserialize(transferredCourseData)
            self.transferredCourses.append(transferredCourse)

        for pastTermData in data.get('pastTerms'):
            pastTerm = PastTerm()
            pastTerm.deserialize(pastTermData)
            self.pastTerms.append(pastTerm)
