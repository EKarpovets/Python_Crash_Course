sandwich_orders = ['pastrami','tuna', 'pastrami', 'ham', 'cheese', 'pastrami', 'vegetarian']
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made you a " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)