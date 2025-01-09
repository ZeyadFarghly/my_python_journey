from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('ping pong game')
screen.tracer(0)
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's') 
game_finished = False
while not game_finished:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()
    if ball.xcor() >= 390 or ball.xcor() <= -390:
        scoreboard.update_score(ball.reset())
    if right_paddle.distance(ball) < 50 and ball.xcor() > 330:
        ball.bounce()
    if left_paddle.distance(ball) < 50 and ball.xcor() < -330:
        ball.bounce()
screen.exitonclick()

