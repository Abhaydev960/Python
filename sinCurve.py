import turtle
import math

screen = turtle.Screen()
screen.title("Sine Curve at Different Angles")
screen.setup(width=800, height=500)

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Draw axes
pen.penup()
pen.goto(-350, 0)
pen.pendown()
pen.goto(350, 0)
pen.penup()
pen.goto(0, -180)
pen.pendown()
pen.goto(0, 180)

# Draw sine curves for 90, 180 and 360 degrees
colors = ["blue", "red", "green"]

for degree, color in zip([90, 180, 360], colors):
    pen.color(color)
    pen.penup()
    for x in range(-350, 351, 2):
        angle = math.radians((x + 350) / 700 * degree)
        y = 100 * math.sin(angle)
        if x == -350:
            pen.goto(x, y)
            pen.pendown()
        else:
            pen.goto(x, y)

pen.penup()
pen.hideturtle()
screen.mainloop()
