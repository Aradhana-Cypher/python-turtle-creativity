import turtle

t= turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("hotpink")

for i in range(36):
    for j in range(5):
        t.forward(100)
        t.right(72)
    t.right(10)
turtle.done()