class Employee:
    def __init__(self,name, ID):
        self.name = name
        self.id = ID

    def display(self):
        print(self.name +" is a employee")

class Manager(Employee):
    def __init__(self,name, ID, department):
        super().__init__(name,ID)
        self.department = department

    def display(self):
            print(self.name +" is a manager")

a = Employee("NH","e01")
b = Manager("ER","M01","HR")
a.display()
b.display()

