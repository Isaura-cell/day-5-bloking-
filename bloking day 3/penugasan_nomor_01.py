import turtle

t = turtle.Turtle()
t.speed(3)

#Persegi Panjang
for i in range(2):
    t.forward(150)
    t.right(90)
    t.forward(100)
    t.right(90)

t.penup()
t.goto(-200, 0)
t.pendown()

#Segitiga
for i in range(3):
    t.forward(100)
    t.left(120) 

t.penup()
t.goto(200, 0)
t.pendown()

#Jajar Genjang
t.forward(100)
t.right(60)
t.forward(80)
t.right(120)
t.forward(100)
t.right(60)
t.forward(80)

turtle.done() 