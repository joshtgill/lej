class AcademicCalculator:

    def __init__(self):
        self.letterGradeValueDirectory = {'A+': 4.0, 'A': 4.0, 'A-': 3.6667,
                                          'B+': 3.3333, 'B': 3.0, 'B-': 2.6667,
                                          'C+': 2.3333, 'C': 2.0, 'C-': 1.6667,
                                          'D+': 1.3333, 'D': 1.0, 'D-': 0.6667,
                                          'D': 0.3333, 'F': 0.0}


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
                scoreCount += course.units * self.letterGradeValueDirectory.get(course.letterGrade)
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
