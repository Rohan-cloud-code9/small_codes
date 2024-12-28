name = input("What is your name -")
print("welcome",name, "to our adventure")
ans1 = input("you are on a dirt road that has come to an end . you can either go left or right, which way would you like to go(left/right)-").lower()

if(ans1 == "left"):
    ans2 = input("you have come across the river so would you like to swim or go by boat(swim/boat) -").lower()
    if(ans2 == "boat"):
        ans3 = input("your boat has a hole in it would you like to fix it or jump into water(fix/jump) -").lower()
        if(ans3 == "fix"):
            print("you fixed the boat and you have reached the destination.")
        elif(ans3 == "jump"):
            print("you have reached to your mom waiting for you at the end of the river")
        else:
            print("not a valid answer you lose!")
    elif(ans2 == "swim"):
        ans3 = input("you have seen a crocodile and its coming towards you would you like to die or get help by rohan(die/help)-").lower()
        if(ans3 == "die"):
            print("Wasted!")
        elif(ans3 == "help"):
            print("congratulation your are alive and rohan the boss helped you.")
        else:
            print("not a valid answer you lose!")         
    else:
        print("not a valid answer you lose!")

elif(ans1 == "right"):
    ans2 =  input("you are infront of a tiger would you like to run or kill that tiger(kill/run)- ").lower()
    if(ans2 == "kill"):
        ans4 = input("you killed the tiger do you want to eat the meat raw or cooked (raw/cooked)-").lower()
        if(ans4 == "raw"):
            print("you reached the deastination but you got died after 1 month")
        elif(ans4 == "cooked"):
            print("you are smart and you won")
        else:
            print("not a valid answer you lose!")
    elif(ans2 == "run"):
        print("you really think you can run faster than the tiger off course you died")
    else:
        print("not a valid answer you lose!")
      
else:
    print("not a valid answer you lose!")

    

