import time
file=str(input("enter the name of the file you want to open :- "))
try:
    f1 = open(f"{file}.txt")
except IOError as e:
    print(e)
else:
    print("teh file is opening.....")
    time.sleep(3)
    with open(f"{file}.txt",'r') as file:
        print(file.read())
finally:
    f1.close()