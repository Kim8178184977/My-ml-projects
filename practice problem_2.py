num=int(input('Enter the number of apples you need :-\n'))
minimum=int(input('Enter the minimum number of student :-\n'))
maximum=int(input('Enter the maximum number of student :-\n'))
for minimun in range (maximum):
    if num%minimum == 0:
        print(f'the {num} no. of apples can'f' be distributed between {minimum} no student')
    elif num%minimum != 0:
        print(f'the {num} no. of apples can'f't be distributed between {minimum} no student')
    minimum+=1