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
restaurant2 = Restaurant("belyash", 'russian')
restaurant3 = Restaurant("china town", "chinese")
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
