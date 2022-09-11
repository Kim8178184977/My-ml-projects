import time 
from functools import lru_cache
Size=int(input("enter the size of cache you want :-"))
#while(True):
@lru_cache(maxsize=Size)
def sample (num):
        time.sleep(1)
        return num
if __name__=='__main__':
    num = int(input("enter the no you want to find fectorial of :- "))
    sample(num)
    print("the next execution will take less time as compare to provious call due to the use of cache")
    sample(num)
    print("the code is executed")