class Restaurant():
    """Trying to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nThe restaurant's name is " + self.restaurant_name.title() + ".")
        print("The restaurant's cuisine type is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("\nThe restaurant " + self.restaurant_name.title() + " is now open.")

restaurant = Restaurant("medvedenka", "italian")
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()