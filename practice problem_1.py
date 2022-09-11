
now= 2022
def future_age(y_birth,y_future):
    return y_future-y_birth
def when_you_turn_100(c_age,c_year):
    return (c_year+100) - c_age
def age_finder(y_birth,c_year):
    return c_year-y_birth

if __name__ == '__main__':
    print('******************welcome to the age calculator*******************')
    print('what you want to find :-\n1.current age\n2.future age\n3.when you turn 100')
    opt=int(input())
    if opt == 1:
        print('enter year of birth :-')
        age=int(input())
        if age > now:
            raise Exception('you are not yet born don''t fool me')
        print(age_finder(age,now))
    elif opt == 2:
        print('entre your age / year of birth :-')
        y_b=int(input())
        if y_b > now:
            raise Exception('you are not yet born don''t fool me')
        y_f=int(input('the year at which you want to know your age :-\n'))
        if y_b >1000:
            print(future_age(y_b,y_f))
        else:
            if y_b>200:
                raise Exception('your entered age is wrong')
            else:
                y = now-y_b
                print(future_age(y,y_f))
    elif opt == 3:
        print('enter your age / year of birth :-')
        age_100=int(input())
        if age_100 > now:
            raise Exception('you are not yet born don''t fool me')
        elif age_100 >1000:
            age= now-age_100
            print(when_you_turn_100(age,now))
            
        else:
            if age_100>200:
                raise Exception('your input age is wrong')
            else:
                y = now-age_100
                a=age_finder(y,now)
                print(when_you_turn_100(a,now))
        