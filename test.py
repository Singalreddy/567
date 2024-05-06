import unittest
from main import *


class TestStaffingCompany(unittest.TestCase):
    def setUp(self):
        self.staffing_company = StaffingCompany()
        self.employee1 = Employee("John Doe", "Software Engineer", 80000)
        self.employee2 = Employee("Jane Smith", "Data Scientist", 90000)
        self.staffing_company.hire_employee(self.employee1)
        self.staffing_company.hire_employee(self.employee2)

    def test_hire_employee(self):
        self.assertEqual(len(self.staffing_company.employees), 2)
        self.assertEqual(self.staffing_company.employees[0], self.employee1)
        self.assertEqual(self.staffing_company.employees[1], self.employee2)

    def test_terminate_employee(self):
        self.staffing_company.terminate_employee("John Doe")
        self.assertEqual(len(self.staffing_company.employees), 1)
        self.assertEqual(self.staffing_company.employees[0], self.employee2)

    def test_adjust_salary(self):
        self.staffing_company.adjust_salary("Jane Smith", 95000)
        self.assertEqual(self.employee2.salary, 95000)

    def test_find_employee_by_name(self):
        found_employee = self.staffing_company.find_employee_by_name("Jane Smith")
        self.assertEqual(found_employee, self.employee2)

        not_found_employee = self.staffing_company.find_employee_by_name("Alice")
        self.assertIsNone(not_found_employee)


if __name__ == '__main__':
    unittest.main()
