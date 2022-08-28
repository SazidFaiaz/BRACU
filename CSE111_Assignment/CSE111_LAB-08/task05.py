
class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60
    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"

class ScienceExam(Exam):
    def __init__(self, marks, time, *part):
        super().__init__(marks)
        self.time = time
        self.part = part
    def __str__(self):
        return f'Marks: {self.marks} Time: {self.time} minutes Number of Parts: {len(self.part)}'
    def examSyllabus(self):
        return f'{part}'

engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())