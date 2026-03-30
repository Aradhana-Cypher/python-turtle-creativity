import turtle
import random
screen=turtle.Screen()
screen.bgcolor("black")

t=turtle.Turtle()
t.speed(0)
t.width(2)

colors=["white","blue","purple","cyan","pink"]
for i in range(800):
    t.pencolor(random.choice(colors))
    t.forward(i*0.5)
    t.right(59)

turtle.done()