#  Spirograph
import turtle as t
import random
tim = t.Turtle()
tim.pensize(1)
tim.speed("fastest")
t.colormode(255)

def random_colour_function():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    random_colour = (r,b,g)
    return random_colour

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colour_function())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()


