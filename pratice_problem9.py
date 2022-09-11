import random
def name_rearrenger(size):
    lis=[]
    for i in range (size):
        name=input('enter the name of the friend :- ').split(" ")
        lis.append(name)
    
    for i in range (size):
        name_jumbler = random.randint(0,size)
        name_jumbler1 = random.randint(0,size)
        print(f"You new names are 😂😂 :- no. {i} {lis[name_jumbler1-1][0]} {lis[name_jumbler-1][1]}")

if __name__=='__main__':
    size = int(input("enter the number of friends :- "))
    name_rearrenger(size)