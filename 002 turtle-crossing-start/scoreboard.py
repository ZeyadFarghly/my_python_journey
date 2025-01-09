FONT = ("Courier", 24, "normal")
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.create()
    def create(self):
        self.write(f'level: {self.level}', False, 'left', FONT)
    def update_level(self):
        self.level+=1
        self.clear()
        self.create()
    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', False, 'center', FONT)