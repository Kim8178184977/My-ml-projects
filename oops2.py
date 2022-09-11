class employee:
    def __init__(self,name,sallry,attendence):
        self.name = name
        self.sallry = sallry
        self.attendence = attendence

Ashutosh = employee("Ashutosh Kumar",2499999,45)
Madhur = employee("Madhur Gupta",250900,48)
def print_it(n) :
    print(f"The name of the Employee is {n.name}\nThe sallary of the employee is {n.sallry}\nThe attendence is {n.attendence}")
    return 0
print_it(Ashutosh)
print_it(Madhur)