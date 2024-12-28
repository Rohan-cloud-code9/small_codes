import turtle
import random
import time

def no_of_turtles():
    racers = 0
    while True:
        numbers = input("Enter the number of racers (2- 10) --")
        if numbers.isdigit():
            numbers = int(numbers)
            if(1< numbers < 11):
                racers += numbers
                return racers
            else:
                print("Number of racers must be between 2 to 10")
        else:
            print("Invalid respond, Try again!")



COLORS= ["yellow", "red", "pink", "brown", "black", "purple", "orange", "cyan", "blue", "green" ]
racers = no_of_turtles()
random.shuffle(COLORS)
colors = COLORS[0:racers]
width, height = 800, 800

def create_turtles():
    turtles = []
    spacingx = width//(racers +1)  
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos((-width//2) + (i+1)*spacingx, -(height//2) +20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def mov_turtles():
    turtles = create_turtles()
    while True:
        for racer in turtles:
            distance = random.randint(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if(y>= (height/2)-10):
                return colors[turtles.index(racer)]
            

def init_turtle():
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title("Turtle - racing")


                


init_turtle()
print("the winner is ", mov_turtles())
time.sleep(2)



    










                
		
        