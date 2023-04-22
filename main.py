
from turtle import  Turtle,Screen
from paddle import Paddle
from ball import ball
from score import Scoreboard
import time
import keyboard ##
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("BONG GAME")
screen.tracer(0)

paddle_left=Paddle((-350,0),"blue")
paddle_right=Paddle((350,0),"red")
bol=ball()


screen.listen()
screen.onkeypress(paddle_right.move_up,"Up")
screen.onkeypress(paddle_right.move_down,"Down")
screen.onkeypress(paddle_left.move_up,"w")
screen.onkeypress(paddle_left.move_down,"s")
scorer=Scoreboard((-200,260),"Blue")
scorel=Scoreboard((200,260),"Red")
game_on=True
while game_on :
    time.sleep(0.06)
    screen.update()
    bol.move()
    if bol.ycor()>280 or bol.ycor()<-280 :
        bol.ybounce()
    
    if bol.distance(paddle_right)<50 and bol.xcor()>320:
        bol.xbounce()
    if bol.distance(paddle_left)<50 and bol.xcor()<-320:
        bol.xbounce()
    if bol.xcor()>=420:
        time.sleep(0.5)

        scorer.increase_score()
        bol.xbounce()
        bol.goto(0,0)
        paddle_left.goto(-350,0)
        paddle_right.goto(350,0)
    
    if bol.xcor()<=-420:
        scorel.increase_score()
        bol.xbounce()
        bol.goto(0,0)
        paddle_left.goto(-350,0)
        paddle_right.goto(350,0)
        time.sleep(0.8)

    if keyboard.is_pressed('Esc'):   
        game_on = False
















screen.exitonclick()



