def recursion (n) :
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return n *recursion(n-1)
""" as we can see the bellow code when we make sertain function in a project and we also want to use 
that particular function in any other project then inspite of creating it again we just import it directly to our project
and use it but while we import it and use the function the function get exucated with the rest of the code as well there for igonering 
that problem .
to the use main function we just write it and just bellow the fuction till where we want it to get executed """
if __name__ =='__main__':
    num=int(input("enter the number :- \n"))
    print(recursion(num))
    print("this is an example of the name&mani function")