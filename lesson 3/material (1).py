from turtle import*


def square():
    for i in range(4):
        forward(100)
        left(90)

for i in range(3):
    square()
    penup()
    forward(110)
    pendown()



# for i in range(3):
#     forward(100)
#     left(120)


exitonclick()