num = int(input("input the number to print the no. :- "))
if num == 5 :
    for i in range (num) :
        for j in range(i):
            print("*",end=" ")
        print(" ")
        i = i + 1
elif num > 5 :
    r =5
    for i in range (r,0,-1) :
        for j in range(1,i):
            print("*",end=" ")
        print(" ")