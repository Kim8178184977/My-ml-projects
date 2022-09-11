# obj = input('enter the name you want to search for')

# if obj.isnumeric():
#     raise Exception('what the fuck are you trying to enter are you dumb')
# else:
#     print(f'hello {obj}')
# the bellow code is the example of the inbuilt excption
num = int(input('enter the number you want to enter :- '))
try:
    num = num/0
    print(num)
except ArithmeticError('you entered a un-logical number'):
    pass
else:
    print('tesk is done')