filename = 'poll_results.txt'

while True:
    print("\nPlease answer the question.")
    print("Enter 'q' any time to quit.")
    result = input("Why do you like programming? ")
    if result == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(result + '\n')