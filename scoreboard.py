from turtle import Turtle
ALIGNMNET = "center"
COLOR = "white"
FONT = ("Courier", 80 , "normal")
class Score():

    def __init__(self):
        self.score1 = Turtle()
        self.score2 = Turtle()
        self.score1Num = 0
        self.score2Num = 0
        self.score1.color("white")
        self.score2.color("white")
        self.score1.penup()
        self.score2.penup()
        self.score1.hideturtle()
        self.score2.hideturtle()
        self.score1.goto(-50, 200)
        self.score2.goto(50, 200)
        self.display_score()

    def display_score(self):
        self.score1.clear()
        self.score2.clear()
        self.score1.write(f"{self.score1Num}", align=ALIGNMNET, font=FONT)
        self.score2.write(f"{self.score2Num}", align=ALIGNMNET, font=FONT)

    def update_score1(self):
        self.score1Num += 1
        self.display_score()

    def update_score2(self):
        self.score2Num += 1
        self.display_score()