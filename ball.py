from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.speed('fast')
        self.x = 15
        self.y = 15
        self.move_speed = 0.1

    def move(self):
        self.x_dir = self.xcor() + self.x
        self.y_dir = self.ycor() + self.y
        self.goto(self.x_dir, self.y_dir)

    def bounce_wall(self):
        self.y = -self.y

    def bounce_paddle(self):
        self.x = -self.x
        self.move_speed *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_paddle()
