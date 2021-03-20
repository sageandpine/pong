from turtle import Turtle

#ALIGNMENT = "center"
#FONT = ("Arial", 17, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("purple")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    #
    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("green")
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    # def increase_score(self):
    #     self.score += 1
    #     self.clear()
    #     self.update_scoreboard()
    #
    #
    #
    #
