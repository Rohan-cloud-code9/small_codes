import turtle
import random


motion = turtle.Turtle()
motion.shape("turtle")
colors = ["yellow", "red", "pink", "brown", "black", "purple", "orange", "cyan", "blue", "green" ]

def init():
    d = 1
    while True:

       screen = turtle.Screen()
       screen.setup(500, 500)
       
       motion.speed(0)
       motion.color("black")
       motion.forward(d)
       motion.right(60)
       motion.forward(d)
       motion.left(60)
       motion.forward(d)
       motion.left(60)
       motion.backward(d)
       motion.right(60)
       motion.forward(d)
       motion.left(60)
       motion.backward(d)
       d += 1
       if(d>500):
            break

init()
    


    
    

    
    
    


