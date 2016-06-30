class Restaurant():
    """Trying to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\nThe restaurant's name is " + self.restaurant_name.title() + ".")
        print("The restaurant's cuisine type is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("\nThe restaurant " + self.restaurant_name.title() + " is now open.")

    def set_number_served(self, new_number_served):
        self.number_served = new_number_served

    def increment_number_served(self, customers_served):
        self.number_served += customers_served


restaurant = Restaurant("medvedenka", "italian")
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.number_served = 2
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(5)
print(restaurant.number_served)

