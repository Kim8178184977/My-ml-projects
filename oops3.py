class Employee2:
    Employee_id = 384875800 
    def __init__(self,name,sallary,attendence):
        self.name = name
        self.sallary = sallary
        self.attendence = attendence
        
    @classmethod
    def chanege_id(clr,new_id):
        clr.Employee_id = new_id
Ashutosh = Employee2("Ashutosh",45000,30)
print(Ashutosh.name)
Ashutosh.chanege_id(59300022)
print(Employee2.Employee_id)