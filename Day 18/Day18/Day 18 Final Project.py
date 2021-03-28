#Damien Hirst Art Project
#  file, preferences, interpreter, import package
import colorgram
colors = colorgram.extract('Image.jpg', 10)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.r
    b = color.rgb.r
    new_color = (r,g,b)
    rgb_colors.append(new_color)

colors_list = (rgb_colors)
#print(color_list)
colors_list = colors_list[3:]  # Remove the white at the start

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(222, 222, 222), (145, 145, 145), (239, 239, 239), (6, 6, 6), (231, 231, 231), (232, 232, 232), (184, 184, 184)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dotcounter in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dotcounter % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180) # Left
        tim.forward(500) # 10 times 50 paces
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

