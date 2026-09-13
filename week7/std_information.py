class Student:
    def __init__(self, name, std_id):
        self.name = name
        self.std_id = std_id

    def display(self):
        print("\n\nStudent name: ", self.name)
        print("Student Id: ", self.std_id)

class PostgraduateStudent(Student):
    def __init__(self, name, std_id, res_topic):
        super().__init__(name, std_id)
        self.res_topic = res_topic

    def display(self):
            print("\n\nPostgraduate Student")
            print("Student name: ", self.name)
            print("Student Id: ", self.std_id)
            print("Student Id: ", self.res_topic)

a = Student("Maru", "s01")
b = PostgraduateStudent("Seyoung", "s02", "How to groom Poodle")
a.display()
b.display()