import turtle

pen = turtle.Turtle()
paper = turtle.Screen()
pen.speed(100)
paper.bgcolor("#9ee0ff")

def move(x,y):
    pen.up()
    pen.goto(x,y)
    pen.down()

move(-750,-200)
pen.fillcolor("#ebd038")
pen.begin_fill()
for i in range (2):
    pen.forward(1500)
    pen.right(90)
    pen.forward(500)
    pen.right(90)
pen.end_fill()

move(550,200)
pen.fillcolor("#FFE600")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

move(-550,-200)
pen.fillcolor("#ebd038")
pen.begin_fill()
pen.left(45)
pen.forward(500)
pen.right(90)
pen.forward(500)
pen.left(45)
pen.end_fill()

move(300,-200)

pen.fillcolor("#009431")
pen.begin_fill()
pen.left(90)
pen.forward(50)
pen.left(90)

for i in range(18):
    pen.right(10)
    pen.forward(5)
pen.right(90)
pen.forward(25)
pen.right(180)
pen.forward(30)

for i in range(18):
    pen.right(10)
    pen.forward(5)
pen.forward(25)
pen.right(180)
pen.forward(25)
pen.right(90)

for i in range(18):
    pen.right(10)
    pen.forward(5)
pen.left(90)
pen.forward(50)
pen.end_fill()

pen.hideturtle()

turtle.done()