
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.moveUp, "Up")
screen.onkey(r_paddle.moveDown, "Down")

screen.onkey(l_paddle.moveUp, "w")
screen.onkey(l_paddle.moveDown, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    # if the ball hit the top or it hit the bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce and reverse the track
        ball.bounce_y()

    # if the ball hit the right or left paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        # bounce and reverse the track
        ball.bounce_x()

    # if the r_paddle miss the ball
    if ball.xcor() > 380:
        # reset the game
        ball.reset_game()
        scoreboard.l_point()

    # if the l_paddle miss the ball
    if ball.xcor() < -380:
        ball.reset_game()
        scoreboard.r_point()

    # decide a winner
    # stop the game
    if scoreboard.announce_winner():
        game_is_on = False


    time.sleep(ball.ball_speed)

screen.exitonclick()