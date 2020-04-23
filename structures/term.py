from structures.course import Course


class Term:

    def __init__(self):
        self.semester = ''
        self.year = 0
        self.courses = []


    def deserialize(self, data):
        self.semester = data.get('semester')
        self.year = int(data.get('year'))
        for courseData in data.get('courses'):
            course = Course()
            course.deserialize(courseData)
            self.courses.append(course)
