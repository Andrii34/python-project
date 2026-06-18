from turtle import *
from random import randint
import time
screen = Screen()
screen.title("turtle game")
screen.setup(width=600,height=600)

player = Turtle()
player.shape("turtle")
player.color("green")
player.up()


train = Turtle()
train.shape("square")
train.color("red")
train.up()
rand_x = randint(-270,270)
train.goto(rand_x,270)


player.goto(0,-250)
player.left(90)

def move_right():
    x = player.xcor()
    player.goto(x+10,-250)

def move_left():
    x = player.xcor()
    player.goto(x-10,-250)


score_writer = Turtle()
score_writer.hideturtle()
score_writer.up()
score_writer.color("black")
score_writer.goto(0,270)


score = 0

score_writer.write(f"Score: {score}",align="center", font=("Arial",18,"bold")  )

screen.listen()
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")


game_over = False


speed=4
while not game_over:
    time.sleep(0.02)
    y=train.ycor()
    train.sety(y-speed)
   

    if train.ycor() < -270:
        rand_x = randint(-270,270)
        train.goto(rand_x,270) 
        speed+=100
        score+=1
        score_writer.clear()
        score_writer.write(f"Score: {score}",align="center", font=("Arial",18,"bold")  )

        
    if player.distance(train)<30:
       game_over=True 

end_text = Turtle()
end_text.hideturtle()
end_text.color("black")
end_text.write("💥 GAME OVER 💥",align="center", font=("Arial",26,"bold")  )


    

screen.mainloop()
