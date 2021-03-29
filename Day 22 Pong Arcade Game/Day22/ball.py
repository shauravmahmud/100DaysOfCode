from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("slowest")
        self.color("white")
        self.shape("circle")
        self.shapesize(1,1)
        self.goto(0,0)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # If 10 then make minus 10 and vice versa

    def bounce_x(self):
        self.x_move *= -1  # If 10 then make minus 10 and vice versa

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()