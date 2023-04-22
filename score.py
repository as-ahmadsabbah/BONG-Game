from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position,name):
        super().__init__()
        self.nameb=name#
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(position)
        self.hideturtle()
        self.write(f"{name} Score: {self.score}", align="center", font=("Times New Roman", 18, "normal"))
    
    def increase_score(self):
        self.clear()
        self.score +=1
        self.score=int(self.score)
        self.write(f"{self.nameb}Score: {self.score}",align="center",font=("Times New Roman",18,"normal"))
    
