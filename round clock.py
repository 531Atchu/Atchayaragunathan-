import turtle
import time
t=turtle
turtle.setup(500,500)
radius=200
t.penup()
t.goto(0,-radius)
t.pendown()
t.circle(radius)
for i in range(12):
    t.penup()
    t.goto(0,0)
    t.setheading(30*i-90)
    t.forward(radius*0.8)
    t.pendown()
    t.forward(radius*0.2)