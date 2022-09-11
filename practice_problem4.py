def is_not_pallendrom(number):
    number +=1
    while not is_pallendrom(number) :
        number+=1
    return number
def is_pallendrom(number):
    return str(number) == str(number)[::-1]
if __name__ == '__main__':
    n = int(input("Enter the length of your string:- "))
    lis=[]
    for i in range (n):
        num = int(input('enter the number :- '))
        lis.append(num)
    for i in range(n):
        
        print(f'The next palandrom of {lis[i]} is {is_not_pallendrom(lis[i])}')