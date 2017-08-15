class Student:
        def __init__(self, n, ID):
            self.name = n
            self.ID_number = ID
            self.test_score = []
            self.average_test_score = 0
        def __str__(self):
            nameInfo = "Name: " + str(self.name)
            IDInfo = "ID number: " + str(self.ID_number)
            tsInfo = "Test Scores: " + str(self.test_score)
            avgInfo = "Average Score: " + str(self.average_test_score)
            return nameInfo + " " + IDInfo + " " + tsInfo + " " + avgInfo
        def addScore(self, score):
            self.test_score.append(score)
            self.average_test_score = sum(self.test_score) / len(self.test_score)
        def avgTScore(self):
            return self.average_test_score

testScoreList = [350, 100, 200, 700]
lengthTestScoreList = len(testScoreList)

student1 = Student("bob", 123)
student1.addScore(100)
student1.addScore(400)
testAvg = student1.average_test_score


student2 = Student("frank", 456)
student2.addScore(300)
student2.addScore(200)
testAvg = student2.average_test_score

class Roster:
    def __init__(self):
        self.studentList = []
        #self.ID_number = ID
    def __str__(self):
        studentlistInfo = "student info: "
        emptyString = ""
        for count in range(len(self.studentList)):
            emptyString = emptyString + "\n" + str(self.studentList[count])

        return studentlistInfo + emptyString
    def addStudent(self, newStudent):
        self.studentList.append(newStudent)
    def deleteStudent(self, student_id):
        for number in range(len(self.studentList)):
            if student_id == self.studentList[number].ID_number:
                del self.studentList[number]
                return True
        return False

studentRoster = Roster()

studentRoster.addStudent(student1)
studentRoster.addStudent(student2)
print(studentRoster)
studentRoster.deleteStudent(123)
print(studentRoster)
