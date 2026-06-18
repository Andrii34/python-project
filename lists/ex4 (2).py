from turtle import*
from random import randint, choice

# =================================================================
# ЗАВДАННЯ НА СПИСКИ ТА TURTLE
# =================================================================

# 1. Створи список з 4 назв кольорів (наприклад, "red", "blue", "green", "yellow").
#    Напиши цикл, який малює квадрат, де кожна сторона має колір зі списку.
# t=Turtle()
# colors = ["red","green","blue","yellow"]
# for c in colors:
#     t.color(c)
#     t.forward(100)
#     t.left(90)
# 2. Маємо список довжин: [10, 20, 30, 40, 50, 60, 70, 80].
#    Напиши цикл, де черепашка малює лінію кожної довжини зі списку,
#    повертаючи на 90 градусів після кожної лінії.
# t=Turtle()
# lengths = [10,20,30,40,50,60,70,80]
# for l in lengths:
#     t.forward(l)
#     t.left(90) 
# 3. Створи порожній список `steps`. За допомогою циклу for додай у нього
#    10 випадкових чисел від 10 до 100. Потім змусь черепашку пройти 
#    вперед на кожну з цих відстаней.
# t=Turtle()
# steps = []

# for i in range(10):
#     number = randint(10,100)
#     steps.append(number)
# for x in steps:
#     t.forward(x)
#     t.left(90)

# 4. Створи список кортежів з координатами: points = [(0,0), (100,100), (-100,100), (0,0)].
#    Використовуй цикл, щоб черепашка послідовно перейшла (метод .goto()) 
#    у кожну з цих точок.
# t=Turtle()
# points = [(0,0), (100,100), (-100,100), (0,0)]
# for p in points:
#     t.goto(p)

# 5. Створи список кольорів. Використовуй метод random.choice(), щоб 
#    черепашка малювала 20 зірок у випадкових місцях випадковим кольором зі списку.
# c = ["red","black","blue","yellow","brown"]
# t = Turtle()
# def star(t):

#     for i in range(5):
#         t.forward(75)
#         t.left(144)

# for e in range(20):
#     rand_color = choice(c)
#     t.color(rand_color)
#     y = randint(-200,200)
#     x = randint(-200,200)
#     t.up()
#     t.goto(x,y)
#     t.down()
#     star(t)



# 6. Напиши програму, де товщина лінії черепашки (width) змінюється 
#    згідно зі списком [1, 3, 5, 10, 20]. Намалюй 5 паралельних ліній.
# n = [1,3,5,10,20]
# t = Turtle()
# for e in range(5):
#     t.width(n[e])
#     # print(n[e])
#     t.forward(50)
#     t.backward(50)
#     t.right(90)
#     t.up()
#     t.forward(30)
#     t.down()
#     t.left(90)
    

# 7. Створи список `angles = [60, 90, 120, 144]`. Попроси користувача ввести 
#    індекс (від 0 до 3). Витягни кут зі списку за цим індексом і 
#    намалюй відповідну геометричну фігуру (трикутник, квадрат і т.д.).
# angles = [60,90,120,144]
# index = int(input("please enter index 0-3"))
# for e in range(5):
#     forward(50)
#     left(angles[index])
# 8. Створи список назв кольорів. Використовуй метод .pop(), щоб у циклі 
#    діставати останній колір зі списку, встановлювати його як колір фону (bgcolor)
#    і малювати коло, поки список не стане порожнім.
# colors = ["red","yellow","black","gray","blue"]

# t = Turtle()

# while colors:
    
#     bgcolor(colors[-1])
#     t.circle(100)
#     colors.pop(-1)
# 9. "Спіраль кольорів": Створи список із 6 кольорів. Напиши цикл на 100 ітерацій, 
#    де колір лінії обирається як: список[i % 6]. На кожному кроці черепашка 
#    йде вперед на `i` пікселів і повертає на 59 градусів.
# colors = ["red","yellow","black","gray","blue","green"]

# t=Turtle()

# for i in range(100):
#     t.color(colors[i%6])
#     t.forward(i)
#     t.left(i)

# 10. Створи список `shapes = ["circle", "square", "triangle", "turtle"]`.
#     Напиши цикл, який проходить по списку, змінює форму черепашки (shape) 
#     на поточну, ставить відтиск на екрані (.stamp()) і відходить на 50 пікселів.
shapes = ["circle", "square", "triangle", "turtle"]

t = Turtle()

for s in shapes:
    t.shape(s)
    t.stamp()
    t.up()
    t.forward(50)
    t.down()




exitonclick()