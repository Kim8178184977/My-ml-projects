
library = {"the 48 laws of power":"library","the atomic habit":"library","war":"library",
           "the jappnese way to live a happy life":"library","power of sub-consiois mind":"library"}


class admin :
    __user_id = "Kim@667";
    __password = 28012003;
    
admin_control={}
usr = admin 
while(True):
    
    print("********************************wellcome to the stark library*************************************")
    print("please tell who you are \n1. Admin\n2. Guest") 
    print()
    opt=int(input())
    if opt == 1:
        print("user_id :-")
        
        id = str(input())
        if id == usr._admin__user_id  :
            print("password :-")
            p=int(input())
            if p == usr._admin__password:
                
                while(1):
                    print("welcome sir/mam \n1.essue a book\n2.check library books\n3.to find oner details\nto exit program ckick 4")
                    opt=int(input())
                    if opt==1:
                        print("plese enter the name of the person want's to borrow the book")
                        person=str(input())
                        book=str(input("the name of the book is :- "))
                        library.update({book:person})
                        add=str(input("enter the owner's address :- "))
                        cont=str(input("enter the contect no of the owner :- "))
                        data=(f"the name is :- {person}\nthe address is :-{add}\nthe contact number is :-{cont}")
                        admin_control.update({person:data})
                    elif opt==2:
                        for key,value in library.items():
                            print("the book name :-",key,"\nit is with :-",value)
                    elif opt==3:
                        usre=str(input("enter the name of the person :-"))
                        print(admin_control.get(usre))
                    else:
                        break
        else:
            break
    else:
        print("whant you want to search \n1.Book in library\n2.donate a book\n3.return a book")
        opt1 = int(input())
        if opt1 == 1:
            print(library.keys())
        elif opt1==2:
            print("enter the book name")
            book = str(input())
            library.update({book:"in library"})
        elif opt1 ==3:
            print("enter the name of the book you want to return")
            book = str(input())
            library.update({book:"in library"})
            print(library.items())
        else:
            print("you chose a wrong option")
