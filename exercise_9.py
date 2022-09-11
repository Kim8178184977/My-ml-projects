import os
print("******************************** Welcome to file name arranger **********************************")
dic=os.getcwd()
print(f"you are in this directory :- {dic}")
dic2 = str(input('Enter the name of the directory you want get access to :- '))
os.chdir(dic2)
die=os.getcwd()
print(f"now you are in :- {die}")
lis=os.listdir()
opt=int(input('1.Do you want to see all the file inside this directory \n2.Do you want to search the name of file costmly\n'))
if opt==1:
    print(lis)
elif opt ==2:
    name_f=str(input("enter the name of the file you want to search :- "))
    def ser(lis,name_f):
        for i in range (len(lis)):
            if lis[i]== name_f:
                return True
        return False
    if ser(lis, name_f):
        print("Found")
    else:
        print("Not Found")
else :
    print('invalid option picked')
print("########################## Hello sir/mam what you want to do with the file in this directory ################################")
option=int(input("1.want to pritify the file by capatilising the names of the file\n2.want to arange the file name and arrange it numarically\n3.custom file nameing\n"))
if option == 1:
    lis_n=[]
    for items in lis:
        lis_n.append(items.upper())
    for i in range (len(lis)):
        os.rename(lis[i],lis_n[i])
    print(os.listdir())
elif option == 2:
    num = 0
    lis_n = []
    lis_new=[]
    for i in range(len(lis)):
        lis_n= lis[i].split('.') 
    for i in range (len(lis)):
        lis_new=f"{lis_n[num]}.{lis_n[num+1]}"
        num = num+2
        for i in range (len(lis)):
            os.rename(lis[i],lis_new[i])
    print(lis_n)
elif option==3:
    old_name=str(input('enter the intial name of the file :-'))
    new_name=str(input('enter the new name of the file you want to change the name of :- '))
    os.rename(old_name,new_name)
else:
    print("in-valid option choose")