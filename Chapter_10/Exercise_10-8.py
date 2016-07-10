def print_file(filename):
    """Print the contents of a file."""
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        message = "Sorry, the file " + filename + " could not be found."
        print(message)
    else:
        for line in lines:
            print(line)

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print_file(filename)



