from turtle import Turtle
from random import randint, choice, randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(.5,1.5)
        self.setheading(180)
        self.color(choice(COLORS))
        self.start()
        self.move_distance = STARTING_MOVE_DISTANCE

    def start(self):
        self.goto(randint(300, 900), randrange(-150, 150, 15))

    def drive(self):
        self.fd(self.move_distance)
        if self.xcor() <= -300:
            self.start()

    def level_up(self):
        self.move_distance += MOVE_INCREMENT
