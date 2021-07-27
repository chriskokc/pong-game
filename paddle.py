from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setpos(position)


    def moveUp(self):
        current_ycor = self.ycor()
        new_ycor = current_ycor + 20
        self.goto(x=self.xcor(), y=new_ycor)


    def moveDown(self):
        current_ycor = self.ycor()
        new_ycor = current_ycor - 20
        self.goto(x=self.xcor(), y=new_ycor)
















