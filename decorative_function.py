# in the bellow code we are calling a function inside a function
def intro(func):
    # as we can see in the paranthesis we are ginving function a function which is decleared at the 6th line 
    def ask():
        print("what is your name")
        func()
        print("my name is ashutosh")
    return ask
@intro# this is a decorator whith the help of this we can put the bellow function in the mid of the ask and func function which will make 
# a sandwich of the functions 
def harsh():
    print("tell me your fucking name")
    
harsh()