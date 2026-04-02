# # # 🔹 1. Variable name can contain letters, numbers, and underscore (_)

# # # ✅ Correct:

# # # name = "John"
# # # age2 = 20
# # # user_name = "Sam"

# # # ❌ Wrong:

# # # user-name = "Sam"   # hyphen not allowed


# # # ⸻

# # # 🔹 2. Variable name cannot start with a number

# # # ❌ Wrong:

# # # 2age = 20

# # # ✅ Correct:

# # # age2 = 20


# # # ⸻

# # # 🔹 3. No spaces allowed in variable name

# # # ❌ Wrong:

# # # my name = "John"

# # # ✅ Correct:

# # # my_name = "John"


# # # ⸻

# # # 🔹 4. Python is case-sensitive

# # # name = "John"
# # # Name = "Sam"

# # # 👉 These are different variables

# # # ⸻

# # # 🔹 5. Do not use Python keywords as variable names

# # # Keywords are special words like if, for, while, True

# # # ❌ Wrong:

# # # if = 10

# # # ✅ Correct:

# # # num = 10


# # # ⸻

# # # 🔹 6. Variable name should be meaningful

# # # ✅ Good:

# # # student_name = "Riya"
# # # marks = 90

# # # ❌ Bad:

# # # x = "Riya"
# # # y = 90


# # # ⸻

# # # 🔹 7. No special characters allowed (@, #, %, etc.)

# # # ❌ Wrong:

# # # price@ = 100

# # # ✅ Correct:

# # # price = 100


# # # ⸻
# # # 🔹 8. You don’t need to declare type in Python

# # # Python automatically understands the type

# # # x = 10        # integer
# # # y = "Hello"   # string
# # # z = 3.5       # float
# # # a = true      # boolean

# # # ⸻

# # # 🔹 9. You can change the value anytime

# # # x = 10
# # # x = "Hello"

# # # 👉 Same variable, different value

# # # ⸻

# # # 🔹 10. Multiple variables can be assigned in one line

# # # a, b, c = 1, 2, 3

# # # Swapping variable values

# # a, b = 10, 20
# # print(a, b)
# # a, b = b, a
# # print(a,b)
# # a, b = 1, 2
# # c = b, a

# # print(a, b)
# # print(c)

# # # a, b, c = 1, 2, 1

# # # print(a, b)
# # # print(b, c)

# # # a, b, c = 1, 2, a

# # # print(a, b)
# # # print(b, c)

# # a = 10
# # b = 50
# # c = a
# # a = b
# # b = c

# # print(a, b)

# # input
# name = input("what is ur name???? ")
# # print(name)
# # print("my name is",name )
# # print("my name is "+name)

# age = int(input("what is ur age???? "))
# # print("I am "+age+" years old")

# print("I am "+name+" and I am "+str(age)+" years old")

print("hello\nnew line")
print("\n")
print("hi")

name = input("what is your name?")
age = input("what is your age?")
nationality = input("what is your nationality?")
print("My name is "+name+"\nI am "+age+" years old and I am "+nationality)