class Employee:
    def __init__(self , name , workingPeriod):
        self.name = name
        self.workingPeriod = workingPeriod

    # def workingPeriod(self):
    #     return self.period

    @classmethod
    def employeeByJoiningYear(cls , name , year):
        cls.name = name
        cls.year = 2022 - year
        return Employee(cls.name , cls.year)

    @staticmethod
    def experienceCheck(time , gender):
        if gender == 'male' and time < 3:
            return 'He is not experienced'
        elif gender == 'male' and time >= 3 :
            return 'He is experienced'
        elif gender == 'female' and time < 3 :
            return 'she is not experienced'
        elif gender == 'female' and time >= 3 :
            return 'she is experienced'

employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))