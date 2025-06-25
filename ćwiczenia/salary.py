class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def count_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def count_salary(self):
        return super().count_salary() + self.bonus


john = Employee('john', 500)
edek = Manager('edek', 500, 1000)

print(john.count_salary())
print(edek.count_salary())
