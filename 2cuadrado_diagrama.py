import turtle
import time

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=800, height=600)
t.speed(1)
t.color("red")

time.sleep(2)

for _ in range(4):
    t.forward(100)
    t.left(90)

turtle.done()
