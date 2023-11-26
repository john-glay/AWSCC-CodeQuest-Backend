exit = 0
list = []

while (exit == 0):
    print("\nOPTIONS:")
    print("1. Add item to the shopping list")
    print("2. View shopping list")
    print("3. Remove item from the shopping list")
    print("4. Quit")

    choice = int(input("\nEnter the number of your choice: "))

    if choice == 1:
        item = input("Enter the item you want to add: ")
        list.append(item)
        print(f"{item} has been added to your shopping list.")

    elif choice == 2:
        print("Your shopping list:")

        for i in range(len(list)):
            print(list[i])

    elif choice == 3:
        item = input("Enter the item you want to remove: ")

        if item in list:
            list.remove(item)
            print(f"{item} has been removed from your shopping list.")
        else:
            print(f"{item} not found in your shopping list.")
        
    elif choice == 4:
        print("\nGoodbye!\n")
        exit = 1

    else:
        print("\n--  Invalid Input! Try Again. --")