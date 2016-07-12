import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        first_name = 'Mario'
        last_name = 'Puzo'
        annual_salary = 60000
        self.my_employee = Employee(first_name, last_name, annual_salary)
        self.default_raise = 5000
        self.raises = [6000, 7000, 8000]

    def test_give_default_raise(self):
        current_salary = self.my_employee.annual_salary + self.default_raise
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, current_salary)

    def test_give_custom_raise(self):
        current_salary = self.my_employee.annual_salary + self.raises[0]
        self.my_employee.give_raise(self.raises[0])
        self.assertEqual(self.my_employee.annual_salary, current_salary)



