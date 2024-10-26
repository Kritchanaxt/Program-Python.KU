
#? Ex.OOP1 - #6

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.name}, Position: {self.position}, Salary: {self.salary}"
    
class Manager(Employee):
    def promote_employee(self, employee, new_position, salary_increase):
        employee.position = new_position
        employee.salary += salary_increase
        print(f"{employee.name} has been promoted to {new_position} with a new salary of {employee.salary}.")

emp1 = Employee("Alice", "Developer", 50000)
manager = Manager("Bob", "Senior Manager", 70000)

print("\n\t\t\tEmployee!!")
print("-" * 60)
print(emp1)
print("-" * 60)
print(manager)
print("-" * 60)
manager.promote_employee(emp1, "Lead Developer", 10000)
print("-" * 60)
print(emp1)
print("-" * 60)


