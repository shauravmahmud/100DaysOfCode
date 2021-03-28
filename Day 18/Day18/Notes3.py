#Draw a random walk
import turtle as t
import random
tim = t.Turtle()


directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")

t.colormode(255)

def random_colour_function():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    random_colour = (r,b,g)
    return random_colour

for _ in range(150):
    tim.color(random_colour_function())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()

my_tuple = (1,3,8)  # Tuples are carved in stone
print(my_tuple[0])

# You cannot then reassign something in a Tuple. (Item assignment)
# Tuples are immutable

converted_list = list(my_tuple)

my_list = [0,1,2]
print(my_list)

