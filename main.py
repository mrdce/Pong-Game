from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(1080, 720)
screen.bgcolor('black')
screen.title('pong')
screen.tracer(0)

paddle_r = Paddle(510, 0)
paddle_l = Paddle(-520, 0)
ball = Ball()
score = Score()

screen.update()

screen.listen()
screen.onkeypress(paddle_r.up, 'Up')
screen.onkeypress(paddle_r.down, 'Down')
screen.onkeypress(paddle_l.up, 'w')
screen.onkeypress(paddle_l.down, 's')

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_wall()
    if (ball.xcor() < -480 and ball.distance(paddle_l) < 54) \
            or (ball.xcor() > 480 and ball.distance(paddle_r) < 54):
        ball.bounce_paddle()
        ball.move_speed /= 1.7

    if ball.xcor() < -525:
        ball.ball_reset()
        score.point_to_r()
    if ball.xcor() > 520:
        ball.ball_reset()
        score.point_to_l()


screen.exitonclick()
