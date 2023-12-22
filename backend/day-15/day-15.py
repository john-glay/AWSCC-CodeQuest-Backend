import json

exit_program = False

# Option User Input Handler.
def user_input():
    while True:
        try:
            return int(input("\nEnter the number of your choice: "))
        except ValueError:
            print("\n       Please enter a valid integer!")

# Website Input Handler.
def website_input():
    return input("\nEnter website: ")

# Website Checker
def is_existing(website):
    with open(r'C:\Users\johng\Documents\.College\AWS\AWSCC-CodeQuest-Backend\backend\day-15\data.json', 'r') as f:
        data = json.load(f)
        if website in data:
            return True
        else:
            print("\n   Website not found. Please try again!   ")
        return False

# ADD a Password, Email, and Name of Website.
def add():
    print("\n   ----  ADD USERNAME AND PASSWORD  ----")
    website = input("\nEnter name of website: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    new_data = {
        website: [{
            'email': email,
            'password': password
        }]
    }

    with open(r'C:\Users\johng\Documents\.College\AWS\AWSCC-CodeQuest-Backend\backend\day-15\data.json', 'r') as f:
        data = json.load(f)
    
    if website in data:
        data[website].append({'email': email, 'password': password})
    else:
        data.update(new_data)

    with open(r'C:\Users\johng\Documents\.College\AWS\AWSCC-CodeQuest-Backend\backend\day-15\data.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("\n            Successfully Added!")

# VIEW all inputs.
def view():
    print("\n============  VIEW ALL INPUTS  ===========")
    with open(r'C:\Users\johng\Documents\.College\AWS\AWSCC-CodeQuest-Backend\backend\day-15\data.json', 'r') as f:
        data = json.load(f)

        for key, val in data.items():
            print(f"\n Website: {key}")
            for i in range(len(val)):
                print(f"\n   Email: {val[i]['email']}")
                print(f"   Password: {val[i]['password']}")
            print("\n==========================================")

# SEARCH for a specific input.
def search(website):
    with open(r'C:\Users\johng\Documents\.College\AWS\AWSCC-CodeQuest-Backend\backend\day-15\data.json', 'r') as f:
        data = json.load(f)
        for key, val in data.items():
            if key == website:
                
                print("\n==========================================")
                print(f"\n Website: {key}")
                for i in range(len(val)):
                    print(f"\n   [{i+1}] Email: {val[i]['email']}")
                    print(f"       Password: {val[i]['password']}")
                print("\n==========================================")
                return True
            
        print("\n   Website not found. Please try again!   ")
        website = website_input()
        search(website)
        return 

# DELETE an existing input.
def delete(website):
    with open(r'C:\Users\johng\Documents\.College\AWS\AWSCC-CodeQuest-Backend\backend\day-15\data.json', 'r') as f:
        data = json.load(f)
        search(website)

        valid_idx = False
        while not valid_idx:
            try:
                num = int(input("\nEnter the number you want to delete: "))
                if 0 <= num-1 < len(data[website]):
                    valid_idx = True
                else:
                    print("\n     Invalid Input. Please try again!")
            except ValueError:
                print("\n       Please enter a valid integer!")
    
        data[website].pop(num-1)

        if len(data[website]) == 0:
            data.pop(website)

    with open(r'C:\Users\johng\Documents\.College\AWS\AWSCC-CodeQuest-Backend\backend\day-15\data.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("\n           Successfully Removed!")

# UPDATE a specific input.
def update(website):
    with open(r'C:\Users\johng\Documents\.College\AWS\AWSCC-CodeQuest-Backend\backend\day-15\data.json', 'r') as f:
        data = json.load(f)
        search(website)

        valid_idx = False
        while not valid_idx:
            try:
                num = int(input("\nEnter the number you want to delete: "))
                if 0 <= num-1 < len(data[website]):
                    valid_idx = True
                else:
                    print("\n     Invalid Input. Please try again!")
            except ValueError:
                print("\n       Please enter a valid integer!")

        while True:
            to_update = input("\n'email' or 'password': ").lower()

            if to_update in ['email', 'password']:
                break
            else:
                print("\n Please enter 'email' or 'password' only!")
        new_val = input(f"\nEnter your new {to_update}: ")
        data[website][num-1][to_update] = new_val

    with open(r'C:\Users\johng\Documents\.College\AWS\AWSCC-CodeQuest-Backend\backend\day-15\data.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("\n           Successfully Updated!")

# Option Handler.
def option(choice):
    global exit_program

    while choice not in [1, 2, 3, 4, 5, 6]:
        print("\n     Invalid Input. Please try again!")
        choice = user_input()

    if choice == 1:
        add()
    elif choice == 2:
        view()
    elif choice == 3:
        print("\n  ----  SEARCH FOR A SPECIFIC INPUT  ----")
        website = website_input()
        search(website)
    elif choice == 4:
        print("\n   ----  DELETE AN EXISTING INPUT  ----")
        existing = False
        while not existing:
            website = website = website_input()
            existing = is_existing(website)
        delete(website)
    elif choice == 5:
        print("\n    ----  UPDATE A SPECIFIC INPUT  ----")
        existing = False
        while not existing:
            website = website = website_input()
            existing = is_existing(website)
        update(website)
    elif choice == 6:
        print("\n+----------------------------------------+")
        print("|                                        |")
        print("|   Thank you for using the program!!!   |")
        print("|                                        |")
        print("+----------------------------------------+\n")
        exit_program = True

# Menu
while not exit_program:
    print("\n+----------  PASSWORD MANAGER  ----------+")
    print("|                                        |")
    print("|   Options:                             |")
    print("|      [1] Add Username and Password     |")
    print("|      [2] View                          |")
    print("|      [3] Search                        |")
    print("|      [4] Delete                        |")
    print("|      [5] Update                        |")
    print("|      [6] Exit                          |")
    print("|                                        |")
    print("+----------------------------------------+")

    choice = user_input()

    option(choice)