def fibunachi(n):
    if n == 1  :
        return 0
    elif n == 2:
        return 1
    else:
        return fibunachi(n-1) + fibunachi(n-2)
num = int(input("enter the number \n"))
print(fibunachi(num))