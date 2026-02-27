import turtle

t = turtle.Turtle()
t.speed(3)

#Merah
t.fillcolor("red")
t.begin_fill()
for i in range(2):
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

t.penup()
t.goto(0, -100)
t.pendown()

#Putih
t.fillcolor("white")
t.begin_fill()
for i in range(2):
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

turtle.done() 