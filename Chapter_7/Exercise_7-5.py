message = "Please enter a person's age:"
message += "\nEnter 'quit' when you are finished. "
active = True

while active:
    age = input(message)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("The ticket is free.")
        elif age < 12:
            print("The ticket is $10.")
        elif age >= 12:
            print("The ticket is $15.")
