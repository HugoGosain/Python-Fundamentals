import turtle

pen = turtle.Turtle()
screen = turtle.Screen()
pen.speed(100)

# for i in range(12):
#     pen.forward(105)
#     pen.left(30)


pen.fillcolor("#76df4d")
pen.begin_fill()
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.end_fill()

pen.fillcolor("#1e37c5")
pen.begin_fill()
pen.right(90)
pen.forward(10)
pen.left(135)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(135)
pen.forward(10)
pen.right(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.end_fill()
turtle.done()