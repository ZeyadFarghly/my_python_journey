from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_finished = False
while not game_finished:
    time.sleep(.1)
    screen.update()
    snake.move() 
    if snake.snake[0].distance(food) < 15:
        food.refresh()
        scoreboard.score_increase()
        snake.extend()
    if snake.snake[0].xcor() > 295 or snake.snake[0].xcor() < -295 or snake.snake[0].ycor() > 300 or snake.snake[0].ycor() < -300:
        game_finished = True
        scoreboard.game_over()
    for square in snake.snake[1:len(snake.snake)-1]:
        if snake.snake[0].distance(square) < 10:
            game_finished = True
            scoreboard.game_over()
screen.exitonclick()