# count to 10
for i in range(1,11):
    print (i)
# hello 5 times
for i in range(5):
    print ("Hello")
# name 3 times
name = input("what is your name?")
for i in range(3):
    print (name)
# count by 2
for i in range(0,11,2):
    print (i)
# asterisks
amount = int(input("how many asterisks? "))
for i in range(amount):
    print ("*",end=" ")
# coloured circles
import turtle

pen = turtle.Turtle()
screen = turtle.Screen()
pen.speed(100)

# movement function
def move(x,y):
    pen.up()
    pen.goto(x,y)
    pen.down()

move(50,50)
pen.fillcolor("#000000")
pen.begin_fill()
pen.circle(25)
pen.end_fill()

move(0,0)
pen.fillcolor("#FFFFFF")
pen.begin_fill()
pen.circle(25)
pen.end_fill()

move(-50,-50)
pen.fillcolor("#888888")
pen.begin_fill()
pen.circle(25)
pen.end_fill()

turtle.done()