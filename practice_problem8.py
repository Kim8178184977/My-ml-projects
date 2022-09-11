import random


def wrong_cal(number):
    table = [number * (i+1) for i in range(10)]
    wrong = random.randint(4, 9)
    table[wrong] = table[wrong]+random.randint(1, 3)
    return table


def check(table, number):
    point = 0
    tablec = [number*(i+1)for i in range(10)]
    for i in range(10):
        if table[i] == tablec[i]:
            point += 1
        else:
            print(f'your answer is wrong at {i} Index')
            point -= 1
    if point < 10:
        print("fuck you")
    else:
        print('correct solution')
    print('the answer is')
    return tablec


if __name__ == '__main__':
    question = int(input("enter the number :-  "))
    cal = wrong_cal(question)
    answer = check(cal, question)
    print(answer)
