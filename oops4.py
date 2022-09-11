# n=(input("Enter the employee name :- \n"))
class Employee:
    employee_sallry = 20044
    def __init__(self,name,attendence,rank):
        self.name = name
        self.attendence = attendence
        self.rank = rank
        pass
    @classmethod
    def data(clr,string):
        return clr(*string.split("-"))

Ashutosh =Employee.data("Ashutosh Kumar-30-devloper")
n = Ashutosh
print(f"The name of the employee is {n.name}\n The designetion of the employee is {n.rank}\n The attendence of the employee is {n.attendence}\nThe sallary is {n.employee_sallry}")
# print(Ashutosh.name)
# print(Ashutosh.rank)
# print(Ashutosh.attendence)
# print(Ashutosh.employee_sallry)