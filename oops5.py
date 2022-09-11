class Employee:
    Salary_of_the_employee = 24000
    def __init__(self,name,attendence,post):
        self.name = name
        self.attendence = attendence
        self.post = post
        pass
    @classmethod
    def data(clr,string):
        return clr(*string.split("-"))
    @staticmethod
    def addictional_data(string):
        return "this is an use of staticmethod"+string

Staf = Employee.data("Ashutosh-28-Developer")
print(Staf.name)
print(Staf.attendence)
print(Staf.post)
print(Staf.Salary_of_the_employee)
print(Employee.addictional_data("\t fuck you"))