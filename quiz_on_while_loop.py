inl=0
while (inl <= 5):
    print("enter the number")
    num = int(input())
    if num < 100 :
        print("try again")
    elif num > 100:
        print("your input is more then 100")
        break
    inl = inl + 1