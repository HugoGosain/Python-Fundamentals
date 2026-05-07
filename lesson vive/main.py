import turtle

pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("#ffffff")

pen.speed(100)

color = input("what color do you want a circle to be??\n                     ")
pen.fillcolor(color)
pen.begin_fill()
pen.circle(90)
pen.end_fill()

pen.hideturtle()
turtle.done()