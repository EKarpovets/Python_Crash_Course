class User():
    """Modelling user profiles."""

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print("\nThe user's name is "+ self.first_name.title() + " " + self.last_name.title() + ".")
        print("He / she is " + str(self.age) + " years old.")
        print("He / she lives in " + self.location.title() + ".")

    def greet_user(self):
        print("\nHello, " + self.first_name.title() + ".")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('ekaterina', 'karpovets', 24, 'moscow')
user2 = User('andrey', 'malgota', 23, 'moscow')
user3 = User('medvedenka', 'malgota', '3', 'moscow')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()

for i in range (1, 11):
    user1.increment_login_attempts()

print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)
