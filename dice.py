import random

def roll():
    value = random.randint(1, 6)
    return value

while True:
    players = input("how many players are playing(1/2/3) -")
    if players.isdigit():
        players = int(players)
        if(1<= players <= 3):
           players = int(players)
           break
        else:
            print("no of players would must be in 1 to 3")
    else:
        print("invalid, try again")
        
players_score = [0 for i in range(players)]



p = 0
for p in range(players):
    current_score = 0
    p += 1
    print("\nplayer", p,"turn has just started!\n")
    while True:
        rolling = input("do you want to roll the dice (y/n)").lower()
        if(rolling == "y"):
            points = roll()
            if(points != 1):
                print("you rolled a", points)
                current_score += int(points)
                if(current_score >= 50):
                    print("your total score is ", current_score)
                    break
            else:
                print("oops you rolled a 1!")
                players_score[p-1] = current_score
                print("your total score is", players_score[p-1])
                break
        elif(rolling == "n"):
                pass
        else:
            print("not a valid command you lose your chance")

max_score = max(players_score)
winning_idx = players_score.index(max_score)
print("the winner is player", winning_idx + 1)




                

        
        
        





    

