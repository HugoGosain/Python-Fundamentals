import turtle

pen = turtle.Turtle()
paper = turtle.Screen()

# score = int(input("what was your test score (no percentage)? "))

# if score >= 70:
#     print("FREE ICE CREAM YAAAAAAAAY")
# else:
#     print("this is why you're a failure")

# You decide to withdraw some money from an ATM. But the ATM only has £20 notes.
# So, check if the amount entered by you can be dispensed properly by the ATM.

# amount = int(input("how much do you want to withdraw? "))
# remainder = amount%20

# if remainder == 0:
#     print("you can withdraw this!")
# else:
#     print("you can NOT withdraw this!")

nsides = int(input("How many sides should the shape have? "))
angle = 360/nsides

def shape(nsides,angle):
    for i in range (nsides):
        pen.forward(100)
        pen.left(angle)

shape(nsides,angle)

turtle.done()