import pydoc
a = int(5)
b = int(3)
cal = sum ((a,b))# here sum is a pre bilt or in-bilt functin to perform the sum of two or more then two number
print(cal)
# now we will see self-made functio or we can say how you can write a function
#in the bellow code we have try to make a function
def func_1(a,b):# the things which we have written in the parnthesis is the input the function will take
    print("this is a self made function")
    #in the bellow code we have just crate a variabel and we assinged it a value or a result of some kind of oppration
    ava=(a+b)/2
    #the bellow code is a return function which will return the value of ava when we call this function
    return int(ava)
print(func_1(a,b))
#now we will see what is doc-string
def func_2(a,b):
    """this is the way to call a doc-string\n 
    \t this function is designed to find remender of some number """
    r = a%b
    return(r)
print(func_2(a,b))
print(pydoc.doc(func_2))