from turtle import*

turtles = []

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()



turtles.append(t4)
turtles.append(t1)
turtles.append(t2)
turtles.append(t3)

for t in turtles:
    t.up()

t1.setx(-200)
t2.setx(-50)
t3.setx(80)
t4.setx(200)

for t in turtles:
    t.down()

def star(t):

    for i in range(5):
        t.forward(100)
        t.left(144)

for t in turtles:
    t.color("red")
    star(t)







print(turtles)

exitonclick()