from turtle import Turtle

# The essential score to win the game
WINNING_SCORE = 15

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()


    def update_score(self):
        # clear everything before writing
        self.clear()
        # go to a suitable place first before writing
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier",80,"normal"))
        # go to a suitable place first before writing
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier",80,"normal"))
        self.hideturtle()


    def l_point(self):
        # modify the left score
        self.l_score += 1
        # update it afterwards
        self.update_score()


    def r_point(self):
        # modify the left score
        self.r_score += 1
        # update it afterwards
        self.update_score()


    def announce_winner(self):
        if self.l_score == WINNING_SCORE:
            self.goto(0, 0)
            self.write("Player L wins the game", align="center", font=("Courier",40,"normal"))
            return True
        elif self.r_score == WINNING_SCORE:
            self.goto(0, 0)
            self.write("Player R wins the game", align="center", font=("Courier",40,"normal"))
            return True





