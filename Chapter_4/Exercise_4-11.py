my_pizzas = ["pepperoni", "ham and mushrooms", "chicken barbecue"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("derevenskaya")
friend_pizzas.append("margarita")
print("My favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)