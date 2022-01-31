import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key='Up')
# cars.create_car()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.generator_random()
    cars.move()
    # When the turtle hits the top edge of the screen
    if player.ycor() > 300:
        player.reset()
        cars.reset()
        score.increase_level()
        cars.increase_speed()
    # When the turtle collides with a car
    for car in cars.list:
        print(car.xcor())
        if player.distance(car) < 24 and car.xcor() < 60:
            score.game_over()
            game_is_on = False

screen.exitonclick()
