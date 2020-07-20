known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie","Harry"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name? ").strip().capitalize()

    if name in known_users:
        print("Hello, {}!".format(name))
        remove = input("Would you like to be removed from the system? (Y/N): ").upper().strip()
        if remove == "Y":
            known_users.remove(name)
        elif remove == "N":
            print("No problem, welcome back!")
            
    else:
        print("I don't recognize you")
        add = input("Would you like to be added to the system? (Y/N): ").upper().strip()
        if add == "Y":
            known_users.append(name)
        elif add  == "N":
            input("No probem, have a nice day!")

        

