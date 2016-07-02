"""Admin class"""

from user import User

class Privileges():
    def __init__(self, privileges=['can add post', 'can ban users', 'can delete post', 'can change profile information']):
        self.privileges = privileges

    def show_privileges(self):
            print("The administrator has the following privileges: " + str(self.privileges))


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()