from cgi import test
import random

num= int(input('Enter the lower limit :- '))
num1= int(input('Enter the upper limit :- '))
number=random.randrange(num,num1)
score=[]

p = 0
while not p == 2:
    i = 1
    while True:
        opt = int(input('Enter your guess :-'))
        if opt < number:
            print(f'guess a gretter number then {opt}')
        elif opt > number:
            print(f'guess a smaller number then {opt}')
        else:
            print('**YOU WON THE GAME**')
            break
        i+=1
    print(f'Player won the match in {i} chances')
    score.append(i)
    p+=1

    
if score[0] > score[1]:
    print('player 1 won the match')
elif score[0]<score[1]:
    print('player 2 won the match')
else:
    print('Draw')


