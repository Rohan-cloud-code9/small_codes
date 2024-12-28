import random

options = ["rock", "paper", "scissors"]
user_score = 0
comp_score = 0

while True:
    number = random.randint(0, 2)
    comp_input = options[number]
    user_input = input("chooose one rock/paper/scissors or press anything else to quit -")
    
    if(user_input == "rock" and  comp_input == "paper"):
        print("computer -" ,comp_input)
        comp_score += 1
    elif(user_input == "rock" and comp_input == "scissors"):
        print("computer -" ,comp_input)
        user_score += 1
    elif(user_input == "rock" and comp_input == "rock"):
        print("computer -" ,comp_input)
        user_score += 0
    elif(user_input == "paper" and  comp_input == "paper"):
        print("computer -" ,comp_input)
        comp_score += 0
    elif(user_input == "paper" and comp_input == "scissors"):
        print("computer -" ,comp_input)
        comp_score += 1
    elif(user_input == "paper" and comp_input == "rock"):
        print("computer -" ,comp_input)
        user_score += 1
    elif(user_input == "scissors" and  comp_input == "paper"):
        print("computer -" ,comp_input)
        user_score+= 1
    elif(user_input == "scissors" and comp_input == "scissors"):
        print("computer -" ,comp_input)
        user_score += 0
    elif(user_input == "scissors" and comp_input == "rock"):
        print("computer -" ,comp_input)
        comp_score += 1
    else:
        break
    
print("Your score - ", user_score)
print("computers score", comp_score)

if(user_score > comp_score):
    print("congratulation you won!")
elif(user_score == comp_score):
    print("It was a draw")
else:
    print("computer won")













