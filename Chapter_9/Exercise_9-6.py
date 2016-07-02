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

class IceCreamStand(Restaurant):
    """Representing an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'chewing gum', 'cola', 'watermelon', 'chocolate', 'nutella', 'vanilla']

    def display_flavors(self):
        print("We have the following ice cream flavors: " + str(self.flavors))

stand = IceCreamStand('medvedenka', 'italian')
stand.display_flavors()
