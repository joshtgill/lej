from structures.user import User
from structures.course import Course
from structures.past_term import PastTerm


class Undergrad(User):

    def __init__(self, email = '', password = '', firstName = '', lastName = ''):
        super().__init__(email, password, firstName, lastName)
        self.transferredCourses = []
        self.pastTerms = []


    def deserialize(self, data):
        super().deserialize(data)
        for transferredCourseData in data.get('transferredCourses'):
            transferredCourse = Course()
            transferredCourse.deserialize(transferredCourseData)
            self.transferredCourses.append(transferredCourse)
        for pastTermData in data.get('pastTerms'):
            pastTerm = PastTerm()
            pastTerm.deserialize(pastTermData)
            self.pastTerms.append(pastTerm)
