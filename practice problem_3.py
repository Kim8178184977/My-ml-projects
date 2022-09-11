lis=[]
no_of_items=int(input('enter the number of iteams you want to enter :- '))
for i in range(no_of_items):
    
    cal=int(input('enter the cla of the food products you have:- '))
    lis.append(cal)
lis.sort()
print(lis)
print('the reverse of list usind inbuilt func')
lis2 = lis[:]
lis2.reverse()
print(lis2)
print('the reverse of list using slicing method')
lis1=lis[:]
print(lis1[::-1])

print('with loop')
pos=0
for i in range(len(lis1)//2):
    lis[i],lis[-(i+1)]=lis[-(i+1)],lis[i]
    print(lis)