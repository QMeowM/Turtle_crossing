import time
from turtle import Screen
from tommy import Tommy
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tommy = Tommy()
scoreboard = Scoreboard()

cars = []

for _ in range(20):
    car = Car()
    cars.append(car)

screen.listen()
screen.onkey(fun=tommy.move, key="Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.drive()
        """collision detection"""
        if tommy.distance(car) <= 15 or (20 >= tommy.distance(car) > 15 and
                                         14 >= tommy.ycor() - car.ycor() >= -20):
            scoreboard.game_over()
            game_on = False

    if tommy.ycor() >= 250:
        scoreboard.update_level()
        tommy.reset()
        for car in cars:
            car.level_up()

screen.exitonclick()