import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move, 'Up')
level_up = False
game_is_on = True
move_counter =0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if move_counter == 4:
        car_manager.create_car()
        move_counter = 0
    car_manager.move()    
    for car in car_manager.cars:
        if car.distance(player) < 30 and car.ycor() > player.ycor() - 25 and car.ycor() < player.ycor() + 25:
            game_is_on = False
            scoreboard.game_over()
    if player.is_finish():
        player.reset()
        car_manager.level_up()
        scoreboard.update_level()
    move_counter+=1
screen.exitonclick()
    


