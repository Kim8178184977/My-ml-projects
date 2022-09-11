""" the project is bild a snake water gun game """
import random
list = ["snake","water","gun"]
print("welcome to the snake , water and gun game \n if you want to play the game click (Y)\n if not then click (N)")
dissision = (input().capitalize())
if dissision == "Y": 
    print("the game is started")
    i = 1
    p1 = 0
    p2 = p1+0
    while (i < 10) :
        i = i + 1
        if dissision == 'Y' :
            player_1 = input("choise any one of them \n 1.snake \n 2.water\n 3.gun\n")
            player_2 = random.choice(list)
            if player_1 == "1":
                print("you :-\tsnake")
            elif player_1 == "2":
                print("you :-\twater")
            elif player_1 == "3":
                print("you :-\tgun")
            print("player_2 :-\t",player_2 )
            print("the number of try left :-", 10-i)
            if player_1 =="1" == player_2 == "snake" :
                print("tie")
            elif player_1 == "2" and player_2 == "water":
                print("tie")
            elif player_1 == "3" and player_2 == "gun":
                print("tie")
            elif player_1 == "1" and player_2 == "water":
                print("you won")
                p1=p1+1
            elif player_1 == "2" and player_2 == "gun":
                print("you won")
                p1=p1+1
            elif player_1 == "3" and player_2 == "snake":
                print("you won")
                p1=p1+1
            elif player_1 == "2" and player_2 == "snake":
                print("computer won")
                p2=p2+1
            elif player_1 == "1" and player_2 == "gun":
                print("computer won")
                p2=p2+1
            elif player_1 == "3" and player_2 == "water":
                print("computer won")
                p2=p2+1
            print("score :- ")
            print("you",0+p1)
            print("computer",0+p2)
    if p1 > p2:
        print("you win the game")
    elif p2 > p1:
        print("Better luck next time")
    else:
        print("no one is a winner")
else:
    print("thenks for coming")