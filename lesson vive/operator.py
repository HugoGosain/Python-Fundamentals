# num1 = 15
# num2 = 2
# print(num1/num2)

# # floor division
# print(num1//num2)

# # modulus
# # returns remainder
# print(num1%num2)

# # exponentials
# print(num2**num2)

# # comparison
# # Checks if two values are equal
# print(num1 == num2)

# # unequal to
# print(num1 != num2)

# # logical operator
# # returns True only if both conditions are True
# print(num1 > 2 and num2 < 5)

# # Returns True if at least one condition is True
# print(num1 < 15 or num2 != 5)

# # Reverses the result (True → False, False → True)
# print(not( num1 == num2))

# # assignment operators
# i = 1
# # i = i+5
# i+=5
# print(i)

# #  Order of Precedence (High → Low)
# # () → Parentheses
# # ** → Exponent
# *, /, //, % → Multiplication, Division, Floor Division, Modulus
# +, - → Addition, Subtraction
# Comparison → ==, !=, >, <, >=, <=
# not
# and
# or

# tshirt_price = 10
# pants_price = 20

# tshirt_amount = int(input("How many tshrits were bought? "))
# pants_amount = int(input("How many pants were bought? "))

# tshirt_total = tshirt_price*tshirt_amount
# pants_total = pants_price*pants_amount
# total = tshirt_total+pants_total

# print("total amount paid is "+str(total))

 
# ticket_price = 6
# ticket_amount = 4
# price_paid = 50

# Payment_needed = ticket_price*ticket_amount
# change = price_paid-Payment_needed

# print("The change you should get is "+str(change))

# ppp = change/5

# print (str(ppp))

# num1 = int(input("NUMBER, NOW!!!!!!! "))
# num2 = int(input("NUMBER, NOW!!!!!!! "))
# if num1>num2:
#     print ("True")
# else:
#     print ("False")

num1 = int(input("NUMBER, NOW!!!!!!! "))
num2 = int(input("NUMBER, NOW!!!!!!! "))
operator = input("operation ")

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
elif operator == "%":
    print(num1%num2)
elif operator == "**":
    print(num1**num2)
else:
    print("please enter an OPERATOR")