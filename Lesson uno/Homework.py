# name = input("what is your name?")
# age = input("what is your age?")
# math =int( input("what are your math grades?"))
# science =int( input("what are your science grades?"))

# average = (math+science)/2

# print("Your name is "+name+"you are "+age+".\n Your math grade are "+str(math)+" and your science grade are "+str(science)+". \nYour average grade is "+str(average))

# Create a Python program that:
# Ask the user:
# Customer name
# Number of items purchased
# For 2 items, ask:
# Item 1 price
# Item 2 price
# Convert inputs into proper numeric types.
# Calculate:
# Total cost

name = input("what is your name?        ")
item = input("how many things did you purchase?     ")
item1cost =float( input("how much did the first item cost?      "))
item2cost =float( input("how much did the second item cost?     "))

total = item1cost+item2cost

print("Your name is "+name+" and you bought "+item+" items.\n Your total cost was "+str(total))