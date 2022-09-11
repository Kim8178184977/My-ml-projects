trials = 1
while (trials<4) :
    trials = trials + 1
    option=input("welcome to the number pridiction game\n""if you want to play then :- \n""then chose n for next and x to exit\n")
    if option == "n" :
        print("you will get 5 chances to prdict the number")
        number=int(input("pridect the number between 1 to 100"))
        if number < 69:
            print("oops!! you are close to it")
        elif number<100 and number >= 75 :
            print("guess a samller number then it")
        elif number < 20:
            print("guess a bigger number")
        elif number == 60 and number == 70:
            print("your are very close to it")
        elif number==69:
            print("congratulations you win the game")
            break
    else:
        print("thanks for coming")
        break