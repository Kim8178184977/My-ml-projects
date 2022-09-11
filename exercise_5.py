"""
1. it will ask the user that what he want to do mention his/her dite or exercise
   or want to see his progress
2. it will make a seprate file for every user and will also mention the time of the entry
"""
import datetime
import sys
original = sys.stdout
def date ():
        return datetime.datetime.now()
u1= "Aman"
u2= "Madhur"
u3= "Ashutosh"
print("************************ Welcome to the health management program **************************")
print("\t\t please enter your username so we can fetch your data")
user = input("\tusername :- ").capitalize()
if user == u1 :
    print("\t\t Hi! Aman how can we assist you today ")
    print("what you want ? \n 1. Want to see your performance history \n 2. Want to input the a activity")
    choice = input()
    if choice == "1":
        with open("aman.txt",'r') as file:
            print(file.read())
        with open("aman_dite.txt",'r')as file:
            print(file.read())
    elif choice == "2":
        print("what you want to record ? \n 1. Exercise \n 2. Dite")
        option = input()
        if option == "1":
            with open("aman.txt",'a') as file:
                entry=input()
                sys.stdout = file
                print(date())
                sys.stdout = original
                file.write(entry)
        elif option == "2":
            with open("aman_dite.txt",'a')as file:
                entry = input()
                sys.stdout = file
                print(date())
                sys.stdout = original
                file.write(entry)
        else:
            print("sorry the choice is not available")
elif user == u2 :
    print("\t\t Hi! Madhur how can we assist you today ")
    print("what you want ? \n 1. Want to see your performance history \n 2. Want to input the a activity")
    choice = input()
    if choice == "1":
        with open("madhur.txt",'r') as file:
            print(file.read())
        with open("madhur_dite.txt",'r')as file:
            print(file.read())
    elif choice == "2":
        print("what you want to record ? \n 1. Exercise \n 2. Dite")
        option = input()
        if option == "1":
            with open("madhur.txt",'a') as file:
                entry=input()
                sys.stdout = file
                print(date())
                sys.stdout = original
                file.write(entry)
        elif option == "2":
            with open("madhur_dite.txt",'a')as file:
                entry = input()
                sys.stdout = file
                print(date())
                sys.stdout = original
                file.write(entry)
        else:
            print("sorry the choice is not available")
elif user == u3 :
    print("\t\t Hi! Ashutosh how can we assist you today ")
    print("what you want ? \n 1. Want to see your performance history \n 2. Want to input the a activity")
    choice = input()
    if choice == "1":
        with open("ashutosh.txt",'r') as file:
            print(file.read())
        with open("ashutosh_dite.txt",'r') as file:
            print(file.read())
    elif choice == "2":
        print("what you want to record ? \n 1. Exercise \n 2. Dite")
        option = input()
        if option == "1":
            with open("ashutosh.txt",'a') as file:
                entry=input()
                sys.stdout = file
                print(date())
                sys.stdout = original
                file.write(entry)
        elif option == "2":
            with open("ashutosh_dite.txt",'a') as file:
                entry = input()
                sys.stdout = file
                print(date())
                sys.stdout = original
                file.write(entry)
        else:
            print("sorry the choice is not available")