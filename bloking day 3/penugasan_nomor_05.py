import turtle

t = turtle.Turtle()
t.speed(5)
t.fillcolor("purple")

t.begin_fill()
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

turtle.done() 