sandwich_orders = ['tuna', 'ham', 'cheese', 'vegetarian']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made you a " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print("These are the sandwiches I made for you:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich + ' sandwich')