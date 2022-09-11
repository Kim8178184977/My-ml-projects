from multiprocessing.connection import wait
import time
num=int(input("enter the number :- \n"))
initial = time.time()
for i in range (num) :
    for j in range (i):
        print("#",end=(" "))
    print(" ")
    i+=1
    
print(initial-time.time())

initial2 = time.time()
x = 0
while x<num:
    y = 0
    while y<x:
        print("#",end=(" "))
        y+=1
    print(" ")
    x+=1
    
print(initial2-time.time())


print(time.localtime())
#the out put time
"""5

#
# #
# # #
# # # #
-0.0010137557983398438

#
# #
# # #
# # # #
-0.001100778579711914
"""

for i in range (num):
    print("this is a test program")
    num = num * i
    i+=1
    time.sleep(2)
