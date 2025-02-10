class Employee:
    def __init__(self, name,position, salary):
        self.name = name
        self.position = position
        self.salary = salary
def details(self):
    print("Name:", self.name,"is the",self.position)


employee1 = Employee("John", "CEO", 20000000)
print(employee1.name, employee1.position, employee1.salary)


employee2 = Employee("Jane", "Managing Director", 15000000)
print(employee2.name, employee2.position, employee2.salary)
