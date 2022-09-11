while(True):
    print("what type of comprihension you wanr to see\n1.list comprihension\n2.dictionary comprihension\n3.set comprihension\n4.genrator comprihension")
    opt=int(input())
    if opt == 1:
        num=int(input("enter the value that how long list you want :-  "))
        list1=[i for i in range (num)]
        print(list1)
    elif opt ==2:
        num=int(input("enter the value that how long dictionary you want :-  "))
        dict1={ i:f"item{i}"for i in range (num)}
        print(dict1)
    elif opt ==3:
        itm=str(input("enter the first item of the Set"))
        itm1=str(input("enter the second item of the Set"))
        itm2=str(input("enter the third item of the Set"))
        itm3=str(input("enter the fourth item of the Set"))
        itm4=str(input("enter the fifth item of the Set"))
        set1={set1 for set1 in ["itm","itm1","itm2","itm3","itm4"]}
        print(set1)
    elif opt ==4:
        num=int(input("enter the value that how much number you want to genrate :-  "))
        gen=(i for i in range (num))
        print(gen)
    else :
        print("you have chose wrong option")