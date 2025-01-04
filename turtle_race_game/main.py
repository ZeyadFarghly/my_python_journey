from turtle import Turtle, Screen
import random as rd

turtle = Turtle()
screen = Screen()
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
y_positions = [125, 75, 25, -25, -75, -125]
all_turtles = []
user_color = screen.textinput('make your bet', 'choose your turtle color: ')
for i in range(0, 6):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-300, y_positions[i])
    all_turtles.append(turtle)
if user_color:
    is_race_on = True
color_winner = ''
while(is_race_on):
    for turtle in all_turtles:
        turtle.fd(rd.randint(1, 10))
        x, y = turtle.position()
        if x > screen.window_width():
            is_race_on = False
            screen.bye()
            color_winner, temp = turtle.color()
if color_winner == user_color:
    print(f'{user_color} is really the winner of the race, you guessed right!!')
else:
    print(f'{user_color} did not win the race as you guessd unfortuantely!!, the {color_winner} one is the winner')

