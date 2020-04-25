class CalcService:

    def countUndergradCourses(self, pastTerms):
        undergradCourses = 0
        for pastTerm in pastTerms:
            undergradCourses += len(pastTerm.courses)

        return undergradCourses


    def countUndergradUnits(self, pastTerms, onlyGraded=False):
        undergradUnits = 0
        for pastTerm in pastTerms:
            undergradUnits += self.countTermUnits(pastTerm, onlyGraded)

        return undergradUnits


    def countTermUnits(self, term, onlyGraded=False):
        termUnits = 0
        for course in term.courses:
            if not onlyGraded or course.letterGrade != 'P':
                termUnits += course.units

        return termUnits


    def calcUndergradGpa(self, pastTerms):
        undergradUnits = self.countUndergradUnits(pastTerms, True)
        undergradScore = 0
        for term in pastTerms:
            undergradScore += self.countTermScore(term)

        return round(undergradScore/undergradUnits, 3)


    def calcTermGpa(self, term):
        termUnits = self.countTermUnits(term, True)
        termScore = self.countTermScore(term)

        return round(termScore/termUnits, 3)


    def countTermScore(self, term):
        termScore = 0
        for course in term.courses:
            termScore += self.determineLetterGradeValue(course.letterGrade) * course.units

        return termScore


    def determineLetterGradeValue(self, letterGrade):
        scoreMapping = {'A+': 12/3, 'A': 12/3, 'A-': 11/3,
                        'B+': 10/3, 'B': 9/3, 'B-': 8/3,
                        'C+': 7/3, 'C': 6/3, 'C-': 5/3,
                        'D+': 4/3, 'D': 3/3, 'D-': 2/3,
                        'F': 0/3}

        letterGradeValue = scoreMapping.get(letterGrade)

        return letterGradeValue if letterGradeValue != None else 0
