from admin import Admin, Privileges

administrator = Admin('tyrion', 'lannister', 30, 'westeros')
administrator.privileges.show_privileges()