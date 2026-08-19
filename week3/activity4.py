from activity4_database import create_tables

from activity4_manager import (
    add_student,
    add_lecturer,
    add_subject,
    add_lecture,
    add_enrollment,
    students_per_course,
    students_multiple_courses
)


def menu():
    print("\n==== University Manager ====")
    print("1. Add Student")
    print("2. Add Lecturer")
    print("3. Add Course")
    print("4. Add Lecture")
    print("5. Add Enrollment")
    print("6. Students Registered in Each Course")
    print("7. Students Enrolled in More Than One Course")
    print("8. Exit")


def main():
    create_tables()

    while True:
        menu()
        choice = input("Select an option (1-8): ")

        if choice == '1':
            F_name = input("Enter first name: ")
            L_name = input("Enter last name: ")
            B_date = input("Enter birth date: ")

            add_student(F_name, L_name, B_date)

        elif choice == '2':
            Lecturer_id = int(input("Enter lecturer ID: "))
            L_firstname = input("Enter first name: ")
            L_lastname = input("Enter last name: ")
            L_email = input("Enter email: ")
            L_address = input("Enter address: ")

            add_lecturer(
                Lecturer_id,
                L_firstname,
                L_lastname,
                L_email,
                L_address
            )

        elif choice == '3':
            Subject_code = int(input("Enter course code: "))
            Subject_unit = int(input("Enter course unit: "))
            Subject_udsc = input("Enter course name: ")

            add_subject(
                Subject_code,
                Subject_unit,
                Subject_udsc
            )

        elif choice == '4':
            CC = int(input("Enter lecture code: "))
            Lecture_name = input("Enter lecture name: ")
            Subject_code = int(input("Enter course code: "))
            Lecturer_id = int(input("Enter lecturer ID: "))
            Date = input("Enter lecture date: ")
            Time = input("Enter lecture time: ")

            add_lecture(
                CC,
                Lecture_name,
                Subject_code,
                Lecturer_id,
                Date,
                Time
            )

        elif choice == '5':
            Student_code = int(input("Enter student ID: "))
            CC = int(input("Enter lecture code: "))
            Date_of_enrolment = input("Enter enrolment date: ")

            add_enrollment(
                Student_code,
                CC,
                Date_of_enrolment
            )

        elif choice == '6':
            courses = students_per_course()

            print("\nStudents registered in each course:")

            for course in courses:
                print(course[0], ":", course[1])

        elif choice == '7':
            students = students_multiple_courses()

            print("\nStudents enrolled in more than one course:")

            for student in students:
                print(
                    "Student ID:", student[0],
                    "Name:", student[1], student[2]
                )

        elif choice == '8':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()