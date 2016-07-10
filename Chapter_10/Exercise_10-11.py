import json

favorite_number = input("Enter your favorite number: ")

filename = 'favorite_number.json'
with open(filename, 'w') as file_object:
    json.dump(favorite_number, file_object)

with open(filename) as file_object:
    favorite_number = json.load(file_object)

print("I know your favorite number! It's " + favorite_number + ".")



