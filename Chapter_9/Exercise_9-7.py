class User():
    """Modelling user profiles."""

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print("\nThe user's name is "+ self.first_name.title() + " " + self.last_name.title() + ".")
        print("He / she is " + str(self.age) + " years old.")
        print("He / she lives in " + self.location.title() + ".")

    def greet_user(self):
        print("\nHello, " + self.first_name.title() + ".")

class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = ['can add post', 'can ban users', 'can delete post', 'can change profile information']

    def show_privileges(self):
        print("The administrator has the following privileges: " + str(self.privileges))

administrator = Admin('tyrion', 'lannister', 30, 'westeros')
administrator.show_privileges()