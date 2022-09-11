class employee:
    attendence = 0
    sallary = 0

class programer(employee):
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        pass
    @classmethod
    def attendence_get(clr,add):
        clr.attendence = add
        return 0
    @classmethod
    def add_sallary(clr,sall):
        clr.sallary = sall
        return 0
    @classmethod
    def employee_data(clr,string):
        return clr(*string.split("-"))
    pass
Madhur=programer.employee_data("Ashutosh kumar-developer")
Madhur.attendence_get(31)
Madhur.add_sallary(35000)
print(Madhur.name)
print(Madhur.attendence)
