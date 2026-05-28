# while True:
#     print("RAHHHHHHH")
# g = 1
# while g != 6:
#     print(g)
#     g = g+1
# j = 10
# while j != 4:
#     print(j)
#     j-=1
# i = 1
# while True:
#     print(i)
#     if i == 5:
#         break
#     i+=1
while True:
    convert1 = input("what unit do you want to convert (miles <--> km, pounds <--> ounce)? or type exit to quit ").lower()
    ninput = int(input("what amount do you want to convert? "))

    if convert1 == "exit":
        break
    if convert1 == "miles":
        output = ninput*1.61
        unit = "km"
    elif convert1 == "km":
        output = ninput/1.61
        unit = "miles"
    elif convert1 == "pounds":
        output = ninput*16
        unit = "ounce"
    elif convert1 == "ounce":
        output = ninput/16
        unit = "pounds"
    else:
        print("invalid inputs")

    print(str(ninput),str(convert1)+"is equal to "+str(output),str(unit))