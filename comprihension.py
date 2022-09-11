#there are four types of comprihension 1. list 2. set 3.dictnery 4. genretor
#list comprihension
list1 = [i for i in range (100) if i%4 == 0 ]
print(list1)
#set comprihensipon
vegis = { vegis for vegis in ["tomato","potato","tomato","eggplant","lady finger","potato","onion"]   }
print(vegis)
#dictnery comprihension
dict1 = {i:f"Item{i}"for i in range (5)}
print(dict1)
# dictnery comprihension for raversing the key with value
dict2={ value:key for key,value in dict1.items()}
print(dict2) 
# genrator comprihension 
prime = (i for i in range (100)if i%5==0)
for i in prime:
    print(i,end=(","))