message = "Please enter a topping for your pizza:"
message += "\nEnter 'quit' when you are finished. "
active = True

while active:
    topping = input(message)
    if topping == 'quit':
        active = False
    else:
        print(topping.title() + " will be added to your pizza.")
