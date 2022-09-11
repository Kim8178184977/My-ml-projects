lis = ['roti','chawal','chole','puri','raita','idle','dosa','samber']
order=str(input("enter the food you want to search avability of :- "))
for item in lis:
    if item == order:
        print(order)
        break
else:
    print("the listed item is not in the list of diner")