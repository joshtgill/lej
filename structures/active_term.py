from structures.active_course import ActiveCourse


class ActiveTerm:

    def __init__(self):
        self.semester = ''
        self.year = 0
        self.activeCourses = []


    def deserialize(self, data):
        self.semester = data.get('semester')
        self.year = int(data.get('year'))
        for activeCourseData in data.get('activeCourses'):
            activeCourse = ActiveCourse()
            activeCourse.deserialize(activeCourseData)
            self.activeCourses.append(activeCourse)
