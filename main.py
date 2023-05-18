from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(right_paddle.moveup, 'Up')
screen.onkey(right_paddle.movedown, 'Down')
screen.onkey(left_paddle.moveup, 'w')
screen.onkey(left_paddle.movedown, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50  or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()
        ball.movespeed *= 0.9

    if ball.xcor() > 360:
        scoreboard.rpoint()
        ball.reset()

    if ball.xcor() < -360:
        scoreboard.lpoint()
        ball.reset()


    ball.move()





screen.exitonclick()