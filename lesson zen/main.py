print ("welcome to the Python Calculator!")

while True:
    num1 = int(input("what is the first number? "))
    num2 = int(input("what is the second number? "))
    operation = input("which operation (+, -, *, /) will you be using? ")
    if operation == "+":
        total = num1+num2
        print ("your total is "+str(total))
    elif operation == "-":
        total = num1-num2
        print ("your total is "+str(total))   
    elif operation == "*":
        total = num1*num2
        print ("your total is "+str(total))   
    elif operation == "/":
        total = num1/num2
        print ("your total is "+str(total))   
    else:
        print ("please enter a valid operation")