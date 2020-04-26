from user import User
from course import Course
from past_term import PastTerm


class Undergrad(User):

    def __init__(self, email = '', password = '', firstName = '', lastName = ''):
        super().__init__(email, password, firstName, lastName)
        self.majors = []
        self.minors = []
        self.transferredCourses = []
        self.pastTerms = []


    def serialize(self):
        # Serialize super
        undergradData = super().serialize()

        # Serialize transferred courses
        transferredCoursesData = []
        for transferredCourse in self.transferredCourses:
            transferredCoursesData.append(transferredCourse.serialize())
        undergradData.update({'transferredCourses': transferredCoursesData})

        # Serialize past terms
        pastTermsData = []
        for pastTerm in self.pastTerms:
            pastTermsData.append(pastTerm.serialize())
        undergradData.update({'pastTerms': pastTermsData})

        return undergradData


    def deserialize(self, data):
        super().deserialize(data)
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
