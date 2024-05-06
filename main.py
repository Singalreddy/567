class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.name} - {self.position} - ${self.salary}/year"


class StaffingCompany:
    def __init__(self):
        self.employees = []

    def hire_employee(self, employee):
        self.employees.append(employee)

    def terminate_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                print(f"{name} has been terminated.")
                return
        print(f"Employee with name {name} not found.")

    def adjust_salary(self, name, new_salary):
        for employee in self.employees:
            if employee.name == name:
                employee.salary = new_salary
                print(f"{name}'s salary has been adjusted to ${new_salary}/year.")
                return
        print(f"Employee with name {name} not found.")

    def find_employee_by_name(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None

    def list_employees(self):
        for employee in self.employees:
            print(employee)


if __name__ == "__main__":
    staffing_company = StaffingCompany()

    # Example usage
    employee1 = Employee("John Doe", "Software Engineer", 80000)
    employee2 = Employee("Jane Smith", "Data Scientist", 90000)

    staffing_company.hire_employee(employee1)
    staffing_company.hire_employee(employee2)

    print("List of employees:")
    staffing_company.list_employees()

    # Test termination
    print("\nTerminating an employee:")
    staffing_company.terminate_employee("John Doe")
    staffing_company.list_employees()

    # Test salary adjustment
    print("\nAdjusting salary:")
    staffing_company.adjust_salary("Jane Smith", 95000)
    staffing_company.list_employees()

    # Test searching for an employee
    print("\nSearching for an employee:")
    found_employee = staffing_company.find_employee_by_name("Jane Smith")
    if found_employee:
        print("Employee found:", found_employee)
    else:
        print("Employee not found.")

