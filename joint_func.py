list1=["aman","ashutosh","arayan","madhur"]
#the anove code is the the list when we genraly print with no sapration or we can say without coma 
# or if we want to print a line or string before executing it for that we have to write a for loop  like bellow
sample=" , "
intro = " \nmy name is :- "
# there for inspite of writing a loop we use .jion()
joi = sample.join(list1)
# as we can see the join function call the list one by one join it with the requried string
intro1 = intro.join(list1)
print(joi)
print(intro1)