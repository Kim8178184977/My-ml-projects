list = [["ashutosh",45],["madhur",45],["aman",45],["ansh",45]]
#in the bellow code we have copied the whole list into a dictonery
dict1 = dict(list)
# the bellow code is a for loop function in which we have call the list till its very end 
# we have call it indirectly from with the help of dictonery
for name, num in dict1.items(): 
    print(name ,num)
# the bellow code is a normal or we can say a not very complex kind of for loop
for name, num in list:
    print(name,num)