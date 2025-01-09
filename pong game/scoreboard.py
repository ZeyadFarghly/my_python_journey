from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score_display()
    def score_display(self):
        self.write(f'{self.left_score} | {self.right_score}', False, 'center', ('courier', 20, 'normal'))
    def update_score(self, loser):
        if loser == 1:
            self.right_score+=1
            print(self.right_score)
        else:
            self.left_score+=1
            print(self.left_score)
        self.clear()
        self.score_display()