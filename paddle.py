from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.resizemode("user")
        self.left(90)
        self.shapesize(stretch_len=5)
        self.goto(x, y)

    def up(self):
        if self.ycor() < 290:
            self.fd(20)

    def down(self):
        if self.ycor() > -290:
            self.bk(20)
