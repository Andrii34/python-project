from turtle import *

# =================================================================
# 10 ЗАДАНИЙ: ФУНКЦИИ БЕЗ ПАРАМЕТРОВ (def name():)
# =================================================================

# ЗАДАНИЕ 1: Функция draw_square()
# Напиши функцию, которая рисует квадрат со стороной 100.
# Вызови её в конце файла.
def squere():   
    forward(100)
    left(90) 
    forward(100)
    left(90) 
    forward(100)
    left(90) 
    forward(100)
    left(90)
# squere()
  
# ЗАДАНИЕ 2: Функция draw_triangle()
# Создай функцию, которая рисует равносторонний треугольник 
# (сторона 120, угол поворота 120).
def triangle():
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)

# triangle()
# ЗАДАНИЕ 3: Функция draw_rectangle()
# Создай функцию, которая рисует прямоугольник со сторонами 150 на 80 пикселей.
def rectangle():
    forward(150)
    left(90)
    forward(80)
    left(90)
    forward(150)
    left(90)
    forward(80)
    left(90)

# rectangle()
# ЗАДАНИЕ 4: Функция draw_cross()
# Напиши функцию, которая рисует "плюс" (четыре линии из центра в разные стороны).
# Подсказка: после каждой линии возвращайся в центр с помощью backward().
def cross():
    forward(100)
    backward(100)
    left(90)
    forward(100)
    backward(100)
    left(90)
    forward(100)
    backward(100)
    left(90)
    forward(100)
    backward(100)
    left(90)

# cross()
# ЗАДАНИЕ 5: Функция draw_circle()
# Создай функцию, которая рисует синий круг радиусом 50. 
# Цвет color("blue") пропиши внутри функции.
def draw_circle():
    color("blue")
    circle(50)

# draw_circle()
# ЗАДАНИЕ 6: Функция draw_letter_h()
# Напиши функцию, которая рисует заглавную букву "Н".
def draw_letter_h():
    forward(50)
    left(90)
    forward(50)
    backward(100)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    backward(100)

# draw_letter_h()
# ЗАДАНИЕ 7: Функция move_up()
# Создай "служебную" функцию, которая просто поднимает перо (up()), 
# проходит вперед на 50 пикселей и снова опускает перо (down()).
def move_up():
    up()
    forward(50)
    down()

# move_up()
# ЗАДАНИЕ 8: Функция draw_star()
# Напиши функцию, которая рисует пятиконечную звезду (сторона 100, угол 144).

# ЗАДАНИЕ 9: Функция draw_house()
# Создай функцию, которая рисует домик. Внутри неё вызови 
# сначала draw_square(), а затем draw_triangle().
def draw_hause():
    squere()
    forward(100)
    left(90)
    forward(100)
    left(30)
    triangle()
    

draw_hause()  
# ЗАДАНИЕ 10: Функция draw_pattern()
# Напиши функцию, которая рисует одну "ступеньку" (вперед 30, влево 90, вперед 30, вправо 90).
# Вызови её 5 раз подряд в цикле, чтобы получилась лестница.
# dra=================================================================
def draw_patern():
    left(90)
    forward(30)
    left(90)
    forward(30)
    right(90)
    forward(30)
    left(90)
    forward(30)
    right(90)
    forward(30)
    left(90)
    forward(30)
    right(90)
    forward(30)
    left(90)
    forward(30)
    right(90)
    forward(30)
    left(90)
    forward(30)

# draw_pattern()
exitonclick()

