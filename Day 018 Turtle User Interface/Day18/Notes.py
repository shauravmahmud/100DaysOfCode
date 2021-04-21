from turtle import Turtle as T, Screen
#from turtle import *
#Turtle is packaged in the python library, but not all are.
# Turtles graphic documentation

import heroes  # not initially installed as part of initial library
print(heroes.gen())

Tim = T()
Tim2 = T()
Tim3 = T()

Tim.shape("turtle")
Tim.color("green")

# for _ in range(4):  # repeat four times
#     Tim.forward(100)
#     Tim.right(90)  # angle

for _ in range(15):
    Tim.forward(10)
    Tim.penup()
    Tim.forward(10)
    Tim.pendown()








screen = Screen()
screen.exitonclick()

