# in the bellow code we will see the two type of uproch to perform recursion
# 1. itrated one
# 2. recursion
# the bellow code is a example of factoreal been done with the help of itrater
def itrated (n):
    f = 1
    for i in range (n):
        f = f * (i+1)
    return f
num = int(input("enter the numder \n"))
print(itrated (num))
#the bellow code is a example of the fectoreal been done with the help of a recursion
def recrsive (n):
    if n == 1 :
        return 1
    else:
        return n * recrsive(n-1)
num = int(input("enter the number\n"))
print(recrsive(num))
# the bellow code is example of the fibunacci sequence been called with the help of a itrator 
def fibunachi (n):
    f = 0
    f_1 = 1
    for i in range (num):
        fth = f + f_1
        f = f_1
        f_1= fth 
    return fth
num = int (input("enter number \n"))
print(fibunachi(num))
#the bellow code is a example of fibunachi sequence been called with the help of recursion
def fibunachi1 (num):
    if num == 1:
        return 0
    elif num== 2:
        return 1
    else:
        return fibunachi1(num-1)+fibunachi1(num-2)
num = int (input("enter number \n"))
print(fibunachi1(num))