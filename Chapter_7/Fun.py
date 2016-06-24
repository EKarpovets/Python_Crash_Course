print_message = True
numbers = []
while print_message:
    message = input("Vvedi chislo ili 'stop', brat: ")
    if message == 'stop':
        print("Massiv chisel otsortirovan: " + str(sorted(numbers)))
        print_message = False
    else:
        numbers.append(message)
