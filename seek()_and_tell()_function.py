with open("sample.txt",'a') as file:
    file.write("this is a simple\n")
with open("sample.txt",'r') as file:
    #the bellow code seek takes code to the entered character and then it the code is executed after the entered value
    file.seek(24)
    print(file.readline())
    #the bellow code tells us the number of character in the called line or file
    print(file.tell())