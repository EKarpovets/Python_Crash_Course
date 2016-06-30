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

user1 = User('ekaterina', 'karpovets', 24, 'moscow')
user2 = User('andrey', 'malgota', 23, 'moscow')
user3 = User('medvedenka', 'malgota', '3', 'moscow')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()