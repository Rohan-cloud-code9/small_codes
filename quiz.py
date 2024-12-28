print("Welcome to  computer quiz")
playing = input("do you want to play ?")

if(playing == "yes"):
    print("Okay ! lets play :) ")
else:
    quit()
print("\033[1m" + "here are some rules :")
print("1. answer all the question in small letters")
print("2. if you answered the question correctly you will get 1 point")
print("\033[0m")
score = 0
ans1 = input("First question : What is the full form of CPU ?")
if(ans1 == "central processing unit"):
    print("correct!")
    score += 1
else:
    print("incorrect!")
   
ans2 = input("Second question : What is the full form of HTML ?")
if(ans2 == "hyper text mark-up language"):
    print("correct!")
    score += 1
else:
    print("incorrect!")

ans3 = input("Third question : What is the full form of RAM ?")
if(ans3 == "random access memory"):
    print("correct!")
    score += 1
else:
    print("incorrect!")

ans4 = input("Fourth question : What is the full form of ROM ?")
if(ans4 == "read only memory"):
    print("correct!")
    score += 1
else:
    print("incorrect!")

ans5 = input("Fifth question : Which device is used to input data in a computer?")
if(ans5 == "keyboard"):
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("here is your score :", score)
    









