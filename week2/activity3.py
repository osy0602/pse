class Student:
    #Constructor to initialize the student object
    def __init__(self):
        self.name = ""
        self.age = 0
        self.address = ""
        self.stdID = 0
    def getdata(self):
        #Get Student data from input
        print("===================Enter Student Data===================")
        self.name = input("Enter Student's Name(Q to quit): ")
        if self.name.upper() == 'Q':
            return None
        self.age = input("Enter Student's Age: ")
        self.address = input("Enter Student's Address: ")
        self.stdID = int(input("Enter Student's ID(number): "))
        return {"Name": self.name, "Age": self.age, "Address": self.address, "Student ID": self.stdID}

class StudentList:
    #Constructor to initialize the student list
    #list[dict]
    def __init__(self):
        self.stdList = []

    def getdata(self):
        #Get Student data from input
        while True:
            student = Student().getdata()
            if student is None:
                break
            self.stdList.append(student)
        
    def display(self):
        self.stdList.sort(key=lambda x: x["Student ID"])
        print("==============Student List================")
        for student in self.stdList:
            print(f"Name: {student['Name']}, Age: {student['Age']}, Address: {student['Address']}, Student ID: {student['Student ID']}")

if __name__ == "__main__":
    student_list = StudentList()
    student_list.getdata()
    student_list.display()