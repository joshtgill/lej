class Calculator:

    def __init__(self, dataInterface):
        self.dataInterface = dataInterface


    def calculateCumulativeGpa(self, undergrad):
        score = 0
        units = 0
        for term in undergrad.pastTerms:
            score += self.countTermScore(term)
            units += self.countTermUnits(term, True)

        return score / units


    def calculateTermGpa(self, term):
        score = self.countTermScore(term)
        units = self.countTermUnits(term, True)

        return score / units


    def countTermScore(self, term):
        scoreCount = 0
        for course in term.courses:
            try:
                scoreCount += course.units * self.dataInterface.get('SETTINGS', 'letterGradeValueDirectory').get(course.letterGrade)
            except TypeError:
                continue

        return scoreCount


    def countTermUnits(self, term, gradedOnly=False):
        unitCount = 0
        for course in term.courses:
            if course.letterGrade == 'LW' or (gradedOnly and course.letterGrade == 'P'):
                continue

            unitCount += course.units

        return unitCount
