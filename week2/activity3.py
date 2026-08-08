
class StudentList:
    #Constructor to initialize the student list
    #list[dict]
    def __init__(self):
        self.stdList = []

    def getdata(self):
        #Get Student data from input
        print("================================================")
        name = input("Enter Student's Name(if you want to quit type 'Q'): ")
        if name.upper() == 'Q':
            self.display()
            exit()
        age = input("Enter Student's Age: ")
        address = input("Enter Student's Address: ")
        stdID = input("Enter Student's ID(number): ")
        student = {"Name": name, "Age": age, "Address": address, "Student ID": int(stdID)}
        self.stdList.append(student)
        
    def display(self):
        self.stdList.sort(key=lambda x: x["Student ID"])
        print("==============Student List================")
        for student in self.stdList:
            print(f"Name: {student['Name']}, Age: {student['Age']}, Address: {student['Address']}, Student ID: {student['Student ID']}")

if __name__ == "__main__":
    stdlist = StudentList()
    while True:
        stdlist.getdata()
        