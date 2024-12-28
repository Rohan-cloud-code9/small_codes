import random
right_no = random.randint(1, 100)
guesses = 0
print("the number is from 1 to 100")

while True:
    guesses += 1
    user_no = input("guess the number or press Q to quit : ").lower()
    if(user_no == "q"):
        break
    user_no = int(user_no)
    if(user_no == right_no):
        break
    elif(user_no < right_no):
        print("your number is too small take a bigger guess")
    else:
        print("your number was too big take a smaller guess")

print("you guessed it in ", guesses, "guesses")

       





    




          






    
