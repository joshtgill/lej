import uuid
from structures.course import Course
from structures.term import Term


class User:

    def __init__(self, email = '', password = '', firstName = '', lastName = ''):
        self.uuid = uuid.uuid4()
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.transferredCourses = []
        self.pastTerms = []


    def serialize(self):
        return { 'email': self.email, 'password': self.password, 'firstName': self.firstName, 'lastName': self.lastName }


    def deserialize(self, data):
        self.email = data.get('email')
        self.password = data.get('password')
        self.firstName = data.get('firstName')
        self.lastName = data.get('lastName')
        for transferredCourseData in data.get('transferredCourses'):
            transferredCourse = Course()
            transferredCourse.deserialize(transferredCourseData)
            self.transferredCourses.append(transferredCourse)
        for pastTermData in data.get('pastTerms'):
            pastTerm = Term()
            pastTerm.deserialize(pastTermData)
            self.pastTerms.append(pastTerm)
