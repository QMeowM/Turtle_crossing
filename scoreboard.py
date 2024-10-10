from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)
        self.level += 1

    def game_over(self):
        self.home()
        self.write(arg="Game Over", align="center", font=FONT)

