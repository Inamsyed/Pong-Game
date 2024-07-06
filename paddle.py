from turtle import Turtle
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 10
PADDLE_COLOR = "white"
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color(PADDLE_COLOR)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def move_down(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)