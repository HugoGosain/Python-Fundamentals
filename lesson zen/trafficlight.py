import turtle

pen = turtle.Turtle()
paper = turtle.Screen()
pen.speed(100)

import time

for i in range (5):
    print("Traffic light is RED")
    pen.up
    pen.goto(0,100)
    pen.down
    pen.fillcolor("#ff1111")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()
    pen.clear()
    time.sleep(5)
    print("Traffic light is YELLOW")
    pen.up
    pen.goto(0,50)
    pen.down
    pen.fillcolor("#fff111")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()
    pen.clear()
    time.sleep(5)
    print("Traffic light is GREEN")
    pen.up
    pen.goto(0,0)
    pen.down
    pen.fillcolor("#11ff11")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()
    pen.clear()
    time.sleep(5)