# def addition(num1,num2):
#     output = num1+num2
#     print(output)

# addition(1,1)
# addition(2,2)

# def prime(number):
#     prime=True
#     for i in range(2,number-1):
#         if number%i == 0:
#             prime=False
#     if prime and number>1:
#         print("your number is a PRIME number!!")
#     else:
#         print("your number is NOT a prime number!!")

# prime(97)

# def addition(num1,num2):
#     return num1+num2

# output = addition(7,5)
# print(output)

# def even(numbers):
#     odd=True
#     if numbers%2 == 0:
#         odd=False
#     if odd:
#         print(str(numbers)+"is an odd number!")
#     else:
#         print(str(numbers)+"is an even number!")

# even(7)

# def numberChecker(n):
#     if n%2 == 0:
#         return "even"
#     else:
#         return "odd"

# number = numberChecker(5)
# print (number)

# num1 = 10
# num2 = 15
# num3 = 20

# if num1 > num2 and num1 > num3:
#     1
# elif num1 < num2 and num1 < num3
#     3


# if num1 > num2:
#     if num1 > num3:
#         print("number 1 is biggest")
#     elif num1 < num3:
#         print("number 3 is biggest")
#     else:
#         print("number 1 and 3 are biggest and the same")
# elif num1 < num2:
#     if num1 > num3:
#         print("number 2 is biggest")
#     elif num2 < num3:
#         print("number 3 is biggest")
#     else:
#         print("number 2  and 3 are biggest and the same")

# def numcheck(number):
#     if number%3 == 0:
#         return True
#     else:
#         return False
    
# answer = numcheck(5)
# print(answer)

number = int(input("What number's multiplication table do you want to see? "))

def multiply_table(number):
    for i in range(1,11):
        print (f"{number} * {i} = {number*i}")
multiply_table(number)