from turtle import Turtle, Screen
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
STEP = 20
class Snake:
    def __init__(self):
        self.snake = []
        self.x, self.y = 0, 0
        for _ in range(3):
            square = Turtle()
            square.penup()
            square.shape('square')
            square.color('white')
            square.goto(self.x,self.y)
            self.snake.append(square)
            self.x-=20

    def move(self):
        for square_index in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[square_index-1].xcor()
            new_y = self.snake[square_index-1].ycor()
            self.snake[square_index].goto(new_x, new_y)
        self.snake[0].fd(STEP)

    def extend(self):
        square = Turtle()
        square.penup()
        square.shape('square')
        square.color('white')
        square.goto(self.snake[-1].position())
        self.snake.append(square)
    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)
    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)
    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)
    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    