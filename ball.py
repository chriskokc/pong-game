from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xtrack = 10
        self.ytrack = 10
        self.setpos(0,0)
        self.ball_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.xtrack
        new_y = self.ycor() + self.ytrack
        self.goto((new_x, new_y))


    def bounce_y(self):
        # reverse the track
        self.ytrack *= -1


    def bounce_x(self):
        # reverse the track
        self.xtrack *= -1
        # speed up the ball every turn by shortening time delay
        self.ball_speed *= 0.9


    def reset_game(self):
        self.setpos(0,0)
        self.bounce_x()
        # reset the speed back to normal speed once resetting the game
        self.ball_speed = 0.1







