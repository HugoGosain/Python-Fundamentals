import turtle

pen = turtle.Turtle()
paper = turtle.Screen()
pen.speed(100)
paper.bgcolor("#5555ff")

def move(x,y):
    pen.up()
    pen.goto(x,y)
    pen.down()

move(-750,-200)
pen.fillcolor("#55cc55")
pen.begin_fill()
for i in range (2):
    pen.forward(1500)
    pen.right(90)
    pen.forward(500)
    pen.right(90)
pen.end_fill()

def build(x,y,color,size,size2):
    move(x,y)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(size)
        pen.left(90)
        pen.forward(size2)
        pen.left(90)
    pen.end_fill()

build(-700,-200,"#777777",100,200)
build(-600,-200,"#777777",100,250)
build(-500,-200,"#777777",100,200)
build(-400,-200,"#777777",100,250)
build(-300,-200,"#777777",100,200)
build(-200,-200,"#777777",100,250)
build(-100,-200,"#777777",100,200)
build(0,-200,"#777777",100,250)

turtle.done()