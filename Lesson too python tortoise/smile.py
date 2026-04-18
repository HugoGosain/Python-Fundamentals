import turtle

pen = turtle.Turtle()
screen = turtle.Screen()
pen.speed(100)

pen.fillcolor("#FFEE04")
pen.begin_fill()
# face
pen.circle(120)
pen.end_fill()

# movement function
def move(x,y):
    pen.up()
    pen.goto(x,y)
    pen.down()

move(50,125)

pen.fillcolor("#FFFFFF")
pen.begin_fill()
# right i
pen.circle(20)

move(-50,125)
# left i
pen.circle(20)
pen.end_fill()

move(-60,75)

pen.fillcolor("#000000")
pen.begin_fill()
# smile
pen.forward(120)
pen.right(90)
for i in range(18):
    pen.right(10)
    pen.forward(10)

pen.end_fill()


move(0,300)

pen.write("hello?", font=("Flow Circular", 30, "bold"))

pen.hideturtle()
turtle.done()