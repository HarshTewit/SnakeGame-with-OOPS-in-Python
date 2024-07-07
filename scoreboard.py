from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.clear()
        self.goto(0, 260)
        self.update()


    def update(self):
        self.write(f"Score = {self.score}", True, align="center", font= ("Arial", 24, "normal"))

    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER", True, align="center", font= ("Arial", 24, "normal"))





    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 260)
        self.update()







