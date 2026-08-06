

list1 = []
while True:
    print (" --- To Do List --- \n press any of the following numbers to go to that section \n 1. view tasks \n 2. add task \n 3. remove task \n 4. exit")
    choice = int(input("enter option: "))
    if choice == 1:
        if len(list1) >= 1:
            for i in list1:
                print (f"{i}\n")
        else:
            print ("No Tasks Found\n")

    elif choice == 2:
        task = input("add a task: ")
        list1.append(task)
        print (f"{task} has been added\n")

    elif choice == 3:
        task = input("remove a task: ")
        if task in list1:
            list1.remove(task)
            print (f"{task} has been removed\n")
        else:
            print (f"{task} is not in the list\n")
    
    elif choice == 4:
        break 
    
    else:
        print ("invalid option\n")