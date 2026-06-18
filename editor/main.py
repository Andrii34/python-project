from turtle import*

screen = Screen()
screen.title("paint 2.0")
screen.setup(width=1000,height=600)

t = Turtle()
t.shape("circle")
t.width(3)
t.speed(0)

def draw(x,y):
    t.goto(x,y)


def color_red():
    t.color("red")


def color_black():
    t.color("black")


def color_white():
    t.color("white") 


def color_yellow():
    t.color("yellow")


def color_blue():
    t.color("blue")

def color_green():
    t.color("green")



def squere():
    length = screen.numinput("squere size","input number")
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    screen.listen()


def draw_circle():
    length = screen.numinput("circle size","input number")
    t.circle(length)
    screen.listen()
    


def move(x,y):
    t.up()
    t.goto(x,y)
    t.down() 



def change_width():
    new_width = screen.numinput("line width","imput number")
    t.width(new_width)
    screen.listen()



def draw_triangle():
    length = screen.numinput("triangle size","input number")
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)    
    t.forward(length)
    t.left(120)
    screen.listen()


screen.listen()

t.ondrag(draw)
screen.onscreenclick(move ,btn=1)
screen.onkey(color_red, "r")
screen.onkey(color_black, "b")
screen.onkey(color_white, "w")
screen.onkey(color_yellow, "y")
screen.onkey(color_blue, "x")
screen.onkey(color_green, "g")
screen.onkey(squere, "s")
screen.onkey(change_width, "q")
screen.onkey(draw_circle,"c")
screen.onkey(draw_triangle, "t")

screen.mainloop()

