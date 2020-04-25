from structures.term import Term


class PastTerm(Term):

    def __init__(self):
        super().__init__()
        self.units = 0
        self.gpa = 0


    def deserialize(self, data):
        super().deserialize(data)
