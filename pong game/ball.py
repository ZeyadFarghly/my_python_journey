from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.setheading(45)
        self.penup()
        self.move_speed = 0.005
    def move(self):
        self.fd(1)
    def bounce(self):
        self.move_speed *= 0.9
        self.setheading(self.heading() - 90 % 360) 
    def reset(self):
        self.move_speed = 0.005
        if self.xcor() < 0:
            self.goto(0, 0)
            self.setheading(45)
            return 1
        else:
            self.goto(0, 0)
            self.setheading(135)
            return 2
       