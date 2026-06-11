import random

# number = random.randint(0,1000000)
# print(number)
# generate random 0-1
# print (random.random())

# print(random.randrange(1,11))


while True:
    number = random.randint(0,10)
    guess = int(input("what is your guess? "))
    if number == guess:
        print("YYYYAAAAAAYYY your got it right it was "+str(number))
        break
    elif number > guess:
        print("your number was too low :(")
    else:
        print("your number was too high :(") 