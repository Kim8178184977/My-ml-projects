def check_statement(num):
    if num < 10:
        return num
    else:
        return next_palandrom(num)
def next_palandrom(num):
    while not pallendrom(num):
        num+=1
    return num
def pallendrom(num):
    return str(num) == str(num)[::-1] 

if __name__ == '__main__':
    n = int(input('enter the length of the list :- '))
    lis=[]
    for i in range (n):
        num = int(input('enter the number :- '))
        lis.append(num)
    for i in range (n):
        print(f'the next parabola of {lis[i]} is {check_statement(lis[i])} :- ')