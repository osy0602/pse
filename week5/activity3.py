class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def describe(self):
        return "Person({}, {})".format(self.name, self.age)

class Student(Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age)
        self.student_id = student_id
    def describe(self):
            return "Student({}, {})".format(self.name, self.age)

class Staff(Person):
    def __init__(self, name, address, age, staff_id):
        super().__init__(name, address, age)
        self.staff_id = staff_id
    def describe(self):
            return "Staff({}, {})".format(self.name, self.age)

class General(Staff):
    def __init__(self, name, address, age, staff_id, id, rate_of_pay):
        super().__init__(name, address, age, staff_id)
        self.id = id
        self.rate_of_pay = rate_of_pay
    def describe(self):
            return "General({}, {})".format(self.name, self.age)

class Academic(Staff):
    def __init__(self, name, address, age, staff_id, id, publications):
        super().__init__(name, address, age, staff_id)
        self.id = id
        self.publications = publications
    def describe(self):
            return "Academic({}, {})".format(self.name, self.age)

def main():
    maya = Academic("Maya","Queen st", 54, "s001", "a001", ["Basic programming", "Data structure", "Python coding", "Cloud Engineering", "I don't have umbrella"])
    john = General("John","Wellington", 25, "s002", "g001", 27)
    print("Maya's number of publications: ",len(maya.publications))
    print("John's payrate: ",john.rate_of_pay)
if __name__ == "__main__":
    main()