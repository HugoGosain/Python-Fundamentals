list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print (list1)
# if (list1[1] % 2) != 0:
#         list1.pop(1)
# if (list1[2] % 2) != 0:
#         list1.pop(2)
# if (list1[3] % 2) != 0:
#         list1.pop(3)
# if (list1[4] % 2) != 0:
#         list1.pop(4)
# if (list1[5] % 2) != 0:
#         list1.pop(5)
# if (list1[6] % 2) != 0:
#         list1.pop(6)
# if (list1[7] % 2) != 0:
#         list1.pop(7)
# if (list1[8] % 2) != 0:
#         list1.pop(8)
# if (list1[9] % 2) != 0:
#         list1.pop(9)
# if (list1[0] % 2) != 0:
#         list1.pop(0)
# print (list1)

copylist = []
for item in list1:
    if item % 2 == 0:
        copylist.append(item)
print (copylist)