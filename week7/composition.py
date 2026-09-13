class Department:
    def __init__(self, name):
        self.dept_name = name

    def show_department(self):
        print(self.dept_name)

class University:
    def __init__(self, university_name):
        self.university_name = university_name
        self.departments = [Department("IT"), Department("Engineering"), Department("Economic"), Department("English"), Department("Korean")]

    def show_university(self):
        print(self.university_name + " University\n")
        print("Departments's list")
        for d in self.departments:
            d.show_department()

ds = University("Duksung Women's")
ds.show_university()
