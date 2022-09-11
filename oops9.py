class a :
    name = "ashutosh"  
    def __init__(self):
        self.sec = "Ashutosh"      
class b(a):
    sec = "btech 2-b"
    def __init__(self):
        self.sec = "btech 2-b"
        super().__init__()
    pass
class c(b):
    roll_no = "44"
    def __init__(self):
        self.roll = "34"
        super().__init__()
    pass

A = a()
B = b()
C = c()
print(C.name)