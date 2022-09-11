# the bellow code is the example of try and except function
num=input("enter the value \n")
# according to our knowledge the both input comand will take the values as a string 
num2=input("enter the second value \n")
""" 
now as we can see we have type-casted the variables as a int which mean it will convert the numarical string as 
a integer but what if some one type a alphabet in it then a error will occure and because of that the code written next to it will never
get exeguted there-for we use try and execept 
"""
# the bellow code will force the or command the intreprator to execute it 
try:
    #and if it not get fix in this code it will pass it froward 
    print(int(num)+int(num2))
    #the forwarded code will come in the bellow code and then get executed
    # the code will tell the fault in the input and then execute the code bellow it
except Exception as fault:
    print(fault)
print("hello")