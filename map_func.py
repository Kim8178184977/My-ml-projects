import functools
# --------------------------------------map function ------------------------------------
list1=[1,2,3,4]
for i in range (len(list1)):
    list1[i] = int(list1[i])
map(int,list1)
list1[0] = list1[0]+list1[1]+list1[2]+list1[3]
list1[1] = list1[0]+list1[1]+list1[2]+list1[3]
print(list1)
list1 = [1,2,3,4,5,6,7,8,9]
def square (num):
    return num * num
def cube (num):
    return num*num
func = [square,cube]
for i in range (len(list1)):
    value = list(map(lambda x:x(i),func))
    print(value)
# ------------------------------------filter fuction--------------------------------------
list1 = [1,2,3,4,5,6,7,8,9]

def greater_then(num):
    return num > 5
def equal (num):
    return num == 2
a = list(filter(equal,list1))
a1 = list(filter(greater_then,list1))
print(a,a1)
# ----------------------------------reduce function -----------------------------------------
list1=[1,2,3,4]
print(functools.reduce(lambda x,y: x*y,list1))
print(functools.reduce(lambda x,y:x+y,list1))