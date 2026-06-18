import time

while True:
    time1 = int(input("how long do you want your timer? "))
    for i in range(time1,-1,-1):
        print(time1)
        time1 = time1-1
        if time1 == 4:
            print ("!5 seconds left!")
        if time1 == -1:
            print("TIMES UP!!!!!!!!!!")
        time.sleep(1)