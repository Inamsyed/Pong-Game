from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("orange")
        self.goto(0,0)
        self.x_movement = 10
        self.y_movement = 10

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def wall_collision(self):
        if(self.ycor() >= 280 or self.ycor() <= -280):
            self.y_movement *= -1

    def paddle_collision(self, paddle):
        if (self.distance(paddle) < 50 and self.xcor() > 320):
            self.x_movement *= -1
        if (self.distance(paddle) < 50 and self.xcor() < -320):
            self.x_movement *= -1

    def miss(self, score):
        if(self.xcor() > 380):
            self.goto(0,0)
            score.update_score1()
            self.x_movement = -10
        elif(self.xcor() < -380):
            self.goto(0,0)
            score.update_score2()
            self.x_movement = 10
