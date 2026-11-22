###
# Draws figures with the turtle module
#
import math
import turtle

def draw_square(length):
    pen = turtle.getturtle()
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(length):
    pen = turtle.getturtle()
    pen.forward(length)
    pen.right(135)
    pen.forward(length * math.sqrt(2))
    pen.right(135)
    pen.forward(length)
    pen.right(90)

draw_trangle = draw_triangle

def draw_rectangle(length_a, length_b):
    pen = turtle.getturtle()
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)
