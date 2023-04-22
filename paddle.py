from turtle import Turtle

class Paddle (Turtle):
    def __init__(self,possition,colr):
        super().__init__()
        self.shape("square")#
        self.color(colr)
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(possition)
    
    def move_up(self):
        y=self.ycor()+20
        self.goto(self.xcor(),y)
    
    def move_down(self):
        y=self.ycor()-20
        self.goto(self.xcor(),y)
