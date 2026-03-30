import turtle

screen=turtle.Screen()
screen.bgcolor("gray")
screen.setup(900,700)

t=turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0,-250)#for bottom start
t.pendown()
t.hideturtle()

def tree(branch_len):
    if branch_len>10:
        t.color("black")
        t.width(branch_len/10)
        t.forward(branch_len)

        t.right(25)
        tree(branch_len - 15)

        t.left(50)
        tree(branch_len - 15)

        t.right(25)
        t.backward(branch_len)


tree(100)
turtle.done()