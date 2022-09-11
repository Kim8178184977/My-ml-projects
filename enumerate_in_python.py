l1=["aloo","bhindi","dudh","dumble"]
# calling item of list with loop
i = 1
for item in l1:
    if i%2 != 0:
        print(item)
    i+=1
# calling item of list with enumerate
for index,item in enumerate(l1):
    if index%2 == 0:
        print(item)