###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.getturtle()
pen.speed(5)

## Draw figures
pen.penup()
pen.goto(-250, 150)
pen.pendown()
figures.draw_square(80)

pen.penup()
pen.goto(50, 150)
pen.pendown()
figures.draw_square(50)

pen.penup()
pen.goto(-250, 0)
pen.pendown()
figures.draw_triangle(80)

pen.penup()
pen.goto(50, 0)
pen.pendown()
figures.draw_triangle(50)

pen.penup()
pen.goto(-250, -130)
pen.pendown()
figures.draw_rectangle(100, 60)

pen.penup()
pen.goto(50, -130)
pen.pendown()
figures.draw_rectangle(60, 40)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
