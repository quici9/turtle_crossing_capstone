from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.list = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle('square')
        car.shapesize(stretch_wid=1, stretch_len=3)
        car.penup()
        color = random.choice(COLORS)
        car.color(color)
        car.setheading(180)
        car.goto(300, random.randint(-260, 260))
        self.list.append(car)

    def generator_random(self):
        if random.randint(1, 8) == 1:
            self.create_car()

    def move(self):
        for car in self.list:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def reset(self):
        for car in self.list:
            car.hideturtle()
        self.list.clear()
