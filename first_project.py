import datetime
print("hello world")
print("enter the first value")
#in the bellow code the input() is a input data type which can take any kind of data but by defalt it only take data in string 
#so, for taking int and other kind of data input we have to type-cast it like this(int(input()))
# inpnum=input()
# print("enter the second value")
# inpnum_2=input()
# print("the sum is = ",int(inpnum)+int(inpnum_2))
import datetime
import sys
def date ():
    print(datetime.datetime.now())
print(date())
original = sys.stdout
file=open("aman_dite.txt")
file.close()
with open("aman_dite.txt",'a')as file:
            entry = input()
            sys.stdout = file
            print(date())
            sys.stdout = original
            file.write(entry)