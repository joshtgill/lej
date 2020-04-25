from structures.term import Term


class PastTerm(Term):

    def __init__(self):
        super().__init__()


    def serialize(self):
        coursesData = []
        for course in self.courses:
            coursesData.append(course.serialize())

        termData = super().serialize()
        termData.update({'courses': coursesData})

        return termData


    def deserialize(self, data):
        super().deserialize(data)
