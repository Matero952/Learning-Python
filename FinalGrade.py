class FinalGrade:
    #The easiest way to do this would be to have like a point total and then divide.
    def __init__(self, points, totalPoints, subject, teacher):
        self.points = points
        self.subject = subject
        self.teacher = teacher
        self.totalPoints = totalPoints
        #Creating instances.


    def calculateFinalGrade(self):
        finalGrade = self.points / self.totalPoints
        return finalGrade
    #Function for calculating final grade.


Science = FinalGrade(489, 500, "Biology", "Muzny" )
#Creating object.
print(f"Final Grade:{Science.calculateFinalGrade()}")
#Print statement that uses f strings.