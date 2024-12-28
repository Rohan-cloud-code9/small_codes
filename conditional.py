print("ONLY CAPITAL LETTERS")
light = input("Light name :" )
if(light == "RED"):
    print("stop")
elif(light == "YELLOW"):
    print("go")
elif(light == "GREEN"):
    print("look")
else:
    print("light is broken")

"""second case"""

marks = int(input("marks : "))
if(marks>= 90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print('d')


#single line condition
food = input("food : ")
eat = "yes" if(food == "cake") else "no"
print(eat)


#2nd
Food = input("food : ")
print("sweet") if(Food == "cake" or "jalebi") else print("not sweet")