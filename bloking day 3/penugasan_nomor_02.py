import turtle 

t = turtle.Turtle()
t.speed(3)

#Persegi (Merah)
t.fillcolor("red")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

t.penup()
t.goto(150, 0)
t.pendown()

#Segitiga (Kuning)
t.fillcolor("yellow") 
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

t.penup()
t.goto(-200, -150)
t.pendown()

#Trapesium (Hijau)
t.fillcolor("blue")
t.begin_fill()
t.forward(120)
t.right(60)
t.forward(80)
t.right(60)
t.forward(80)
t.end_fill()

t.penup()
t.goto(0, 150)
t.pendown()

#Segilima (Ungu)
t.fillcolor("purple")
t.begin_fill()
for i in range(5):
    t.forward(100)
    t.right(72)
t.end_fill()

turtle.done() 