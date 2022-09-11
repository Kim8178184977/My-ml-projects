"""
genrators are the types of function which runs the code step by step like we made a genrator to print a no till 1000
the we can call it with a help of for loop or by itrator __next__() till we need a answer from it like we print till 20 or 200 
it will also save or memory space  
"""
def fecto(num):
    fac = 1
    for i in range (num) :
        fac =fac*(i+1)
        yield fac
num=int(input("enter the value you want the fectorial of :- "))
answer=fecto(num)
for i in answer :
    print(i)
def fibonachi(num1):
    fib1 = 0
    fib = 1
    for i in range (2,num1):
        fibth = fib1 + fib
        fib1 = fib
        fib = fibth
        yield fibth
num1=int(input("enter the value you want the fectorial of :- "))
answer1=fibonachi(num1)
for i in answer1:
    print(i)