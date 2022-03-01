from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.level = 1

    def crash(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=("Courier", 24, "normal"))

    def update_level(self):
        self.goto(-230, 250)
        self.write(f"Level: {self.level}", False, align="center", font=("Courier", 24, "normal"))

    def level_up(self):
        self.clear()
        self.level += 1
        self.update_level()



