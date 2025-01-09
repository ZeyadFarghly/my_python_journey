COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
from turtle import Turtle
import random as rd
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        car = Turtle()
        car.setheading(180)
        car.shape('square')
        car.color(rd.choice(COLORS))
        car.shapesize(1, 2)
        car.penup()
        car.goto(280, rd.randint(-240, 280))
        self.cars.append(car)
    def move(self):
        for car in self.cars:
            car.fd(self.speed)
    def level_up(self):
        self.speed += MOVE_INCREMENT
                
