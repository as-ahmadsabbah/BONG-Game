from turtle import Turtle
class ball (Turtle):
    def __init__(self):
        super().__init__()#
        self.shape("circle")
        self.color("white")
        self.penup()
        self.yc=15
        self.xc=11
    
    def move(self):
        x=self.xcor()+self.xc
        y=self.ycor()+self.yc
        self.goto(x,y)
    
    def ybounce (self):
        self.yc*=-1
    
    def xbounce (self):
        self.xc*=-1
