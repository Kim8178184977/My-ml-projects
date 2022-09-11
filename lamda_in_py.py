# way to ude lamda function
# lanbda is a kind of function you define you can say that it is kind of function which can be called by making it as variable
sum = lambda a,b : a+b;
print(sum(2,3))
list1 = [[56,2],[3,49],[5,8]]
# in the bellow code we used the lambda function to replace the first data of the list with 1
list1.sort(key=lambda list1:list1[1])
print(list1)
