class employee :
    attendence = 0
    sallary = 0
class designetion(employee):
    role = 'not given'
class data(employee):
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
    @classmethod
    def employee_details(clr,string):
        return clr(*string.split("-"))
    @classmethod
    def get_designation(clr,role):
        clr.role = role
    @classmethod
    def get_attendence(clr,attendence):
        clr.attendence = attendence
    @classmethod
    def set_sallary(clr,sallary):
        clr.sallary = sallary
        pass
def print_data(self):
    print(f"The name of the employee is :- {self.name}\n The employee id is :- {self.employee_id}\n The designation of the employee is :- {self.role}\n The sallary of the employee is :- {self.sallary} \n The attendence of the employee is :- {self.attendence}")
    pass

Shasank=data.employee_details("Shasank kumar-00349598")
Shasank.get_designation('CEO')
Shasank.get_attendence(28)
Shasank.set_sallary(150000)
print_data(Shasank)