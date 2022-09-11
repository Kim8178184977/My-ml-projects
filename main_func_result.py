# this is the way to call the function of the other file to the working file 
import main_func
print("this is the result file")
num = int(input("enter number :- \n"))
print(main_func.recursion(num))