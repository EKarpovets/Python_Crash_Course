filename = 'guest_book.txt'

while True:
    print("\nPlease enter your name.")
    print("Enter 'q' any time to quit.")
    name = input("Your name is: ")
    if name == 'q':
        break
    else:
        print("Hello, " + name + "!")
        with open(filename, 'a') as file_object:
            file_object.write(name + ' was here.\n')