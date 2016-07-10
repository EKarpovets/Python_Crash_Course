print("Please enter two numbers and I will give you their sum.")
print("Enter 'q' any time to quit.")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError:
    print("You should enter two numbers so that I could sum them.")
else:
    summa = num1 + num2
    print(summa)


