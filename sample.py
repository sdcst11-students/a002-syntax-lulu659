import turtle

s = turtle.getscreen()
t= turtle.Turtle()
s.bgcolor("light blue")
t.fd(200)
t.forward(50)
t.lt(30)
t.forward(100)
t.lt(60)
t.fd(100)
t.lt(90)
t.fd(500)
t.lt(90)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(30)
t.fd(200)

t.pu()
t.goto(-100,200)
t.pd()
t.fd(200)
t.lt(90)
t.fd(300)
t.lt(135)
t.fd(425)
t.lt(135)
t.fd(105)

t.pu()
t.goto(-200,300)
t.pd()
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

t.pu()
t.goto(100,-100)
t.pd()
t.rt(90)
t.fillcolor("blue")
t.begin_fill()
t.circle(200,-130) #semicircle
t.end_fill()

t.pu()
t.goto(50,-50)
t.pd()
t.rt(30)
t.fillcolor("blue")
t.begin_fill()
t.circle(200,130) #semicircle
t.end_fill()

t.pu()
t.goto(100,-50)
t.pd()
t.rt(100)
t.fillcolor("blue")
t.begin_fill()
t.circle(150,100) #semicircle
t.end_fill()

for i in range(30):
    t.rt(90)
