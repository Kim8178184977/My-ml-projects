def searcher():
    with open("aman_dite.txt") as f1:
        flie1=f1.read()
        print("flie scane is completed")
    while (True):
        text = (yield)
        if text in flie1 :
            print("a result for search found in file f1")
        else:
            print("there is no record found for the follwing search")
data = (input("enter the name :-  "))
search = searcher()
next(search)
search.send(data)