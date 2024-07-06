from turtle import Screen, Turtle
from scoreboard import Score
from paddle import Paddle
from ball import Ball
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
import time
def setMidPart(midSection):
    midSection.shape("square")
    midSection.color("white")
    midSection.pensize(10)
    midSection.penup()
    midSection.goto(0, SCREEN_WIDTH / 2)
    midSection.setheading(270)
    midSection.hideturtle()

    i = 0
    while (i < 15):
        midSection.pendown()
        midSection.forward(10)
        midSection.penup()
        midSection.forward(40)
        i += 1


screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

midSection = Turtle()
setMidPart(midSection)

score = Score()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.update()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    ball.wall_collision()
    ball.paddle_collision(r_paddle)
    ball.paddle_collision(l_paddle)
    ball.miss(score)
    if(score.score1Num >= 5 or score.score2Num >= 5):
        game_is_on = False

screen.exitonclick()