# for i in range (2):
#     for j in range (3):
#         print(i,j)

# for row in range (3):
#     for column in range (5):
#         print ("*",end=" ")
#     print ()

# for column in range (1,6,1):
#     for row in range (column):
#         print (row+1,end=" ")
#     print ()

for column in range (1,6,1):
    for row in range (column):
        print ("A",end=" ")
    print ()
    
for row in range (5,0,-1):
    for column in range (row):
        print (column+1,end=" ")
    print ()