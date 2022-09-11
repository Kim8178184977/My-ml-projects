class employee:
    name = "no"
    sallary = 776
    designation = "no"
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        pass
    @classmethod
    def set_sallary(clr,sallary):
        clr.sallary = sallary
    @classmethod
    def set_data(clr,string):
        return clr(*string.split("/"))
    def __add__(self,other):
        return self.sallary + other.sallary
    def __truediv__(self,other):
        return self.sallary/other.sallary
    pass
ashutosh = employee.set_data("Ashutosh/AI developer")
anjlii = employee.set_data("Anjalii/UI designer")
madhur = employee.set_data("Madhur/WEB designer")
ashutosh.set_sallary(450000)
anjlii.set_sallary(500000)
madhur.set_sallary(350000)
def print_desplay(self):
    print(f"The name of the employee is {self.name}\nThe sallary of the employee is {self.sallary}\nThe designation of the employee is {self.designation} \n")
    pass
print_desplay(ashutosh)
print_desplay(anjlii)
print_desplay(madhur)
print(ashutosh+madhur)
print(ashutosh/madhur)