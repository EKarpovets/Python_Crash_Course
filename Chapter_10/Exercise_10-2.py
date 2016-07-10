filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for i in range(1, len(lines)):
    lines[i] = lines[i].replace('Python', 'C')
    print(lines[i].strip())
