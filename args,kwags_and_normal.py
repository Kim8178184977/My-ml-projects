# def sample(*test):
#     for iteam in test:
#         print(iteam)
# sam1=["ashutosh","mashur","rohan","harry"]
# sample(*sam1)
# def sample2(*test1,**test3):
#     for iteam in test1:
#         print(iteam)
#     for key,value in test3.items():
#         print(f"{key} is {value}")

# sam1=["ashutosh","mashur","rohan","harry"]
# sam2={"first name":"Ashutosh","last name":"Kumar","mol.no":"8178184977","email":"ashu32696@gmail.com"}
#sample2(*sam1,**sam2)
def sample3(normal,*test2,**test4):
    print(normal)
    for item in test2:
        print(item)
    for key,value in test4.items():
        print(f"{key} is {value}")
sam1=["ashutosh","mashur","rohan","harry"]
sam2={"first name":"Ashutosh","last name":"Kumar","mol.no":"8178184977","email":"ashu32696@gmail.com"}
sam3="this was a complete step by step explation of the term arga , kwags and normal"
sample3(sam3,*sam1,**sam2)
#the complete explation is bellow 
""" the term args,kwags and normal is just a kind of function ,but all of them have different use's and function's at there own limitation
1. args:- syntex *(name of var) it takes the data in the form of tuples which mean it talks multiple data in a single variable
2. kwags :- syntex **(name of var) it takes the data in the form of key and values like dictonery
3. normal :- the is just like its name normal it is just a var 
the way to call it is like this
                        def (name of function)(normal,*args,**kwags)pass:-kpGvsE2rL26GBS8
"""
