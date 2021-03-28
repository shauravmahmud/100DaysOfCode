from turtle import Turtle as T, Screen
#from turtle import *
#Turtle is packaged in the python library, but not all are.
# Turtles graphic documentation
import random

Tim = T()

Tim.shape("turtle")
Tim.color("green")


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        Tim.forward(100)
        Tim.right(angle)

for shape_side_n in range(3,11):  # Stop number excluded
    Tim.color(random.choice(colours))
    draw_shape(shape_side_n)
