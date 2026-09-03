from college_db import create_tables

from college_dbmanager import (
    add_student,
    add_lecturer,
    student_detail,
    lecturer_detail,
    add_course,
    enroll_student,
    student_course,
    lecturer_courses,
    view_students,
    view_lecturers
)


def menu():
    print("\n==== Welcome to College System ====")
    print("1. Register User")
    print("2. Login User")
    print("3. Admin Page")
    print("4. Exit")


def main():

    create_tables()

    while True:

        menu()
        choice = input("Select an option (1-4): ")

        # Register
        if choice == '1':

            print("\n==== Are you Student or Lecturer? ====")
            print("1. Student")
            print("2. Lecturer")

            user_type = input("Select an option (1-2): ")

            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")

            if user_type == '1':

                add_student(name, phone, address)

            elif user_type == '2':

                add_lecturer(name, phone, address)

            else:

                print("Invalid choice.")

        # Login
        elif choice == '2':

            print("\n==== Login ====")

            print("1. Student")
            print("2. Lecturer")

            user_type = input("Select an option (1-2): ")

            user_id = int(input("Enter user ID: "))
            name = input("Enter name: ")

            if user_type == '1':

                student = student_detail(user_id, name)

                if student:

                    print("\nStudent details:")
                    print("ID:", student[0])
                    print("Name:", student[1])
                    print("Phone:", student[2])
                    print("Address:", student[3])

                    courses = student_course(user_id)

                    print("\nMy Courses:")

                    for course in courses:
                        print(
                            "Course ID:", course[0],
                            "| Name:", course[1],
                            "| Location:", course[2],
                            "| Time:", course[3],
                            "| Lecturer:", course[4]
                        )

                else:

                    print("Student not found.")

            elif user_type == '2':

                lecturer = lecturer_detail(user_id, name)

                if lecturer:

                    print("\nLecturer details:")
                    print("ID:", lecturer[0])
                    print("Name:", lecturer[1])
                    print("Phone:", lecturer[2])
                    print("Address:", lecturer[3])

                    courses = lecturer_courses(user_id)

                    print("\nMy Courses:")

                    for course in courses:
                        print(
                            "Course ID:", course[0],
                            "| Name:", course[1],
                            "| Location:", course[2],
                            "| Time:", course[3],
                        )

                else:

                    print("Lecturer not found.")

            else:

                print("Invalid choice.")

        # Admin
        elif choice == '3':

            print("\n==== Admin Page ====")
            print("1. Create Course")
            print("2. Enroll Student")
            print("3. View All Students")
            print("4. View All Lecturers")
            print("5. Exit Admin Page")

            admin_choice = input("Select an option (1-3): ")

            if admin_choice == '1':
                name = input("Enter course name: ")
                location = input("Enter course location: ")
                time = input("Enter course time: ")
                lecturer_id = int(input("Enter lecturer ID: "))

                add_course(
                    name,
                    location,
                    time,
                    lecturer_id
                )

            elif admin_choice == '2':

                student_id = int(input("Enter student ID: "))
                course_id = int(input("Enter course ID: "))

                enroll_student(
                    student_id,
                    course_id
                )

            elif admin_choice == '3':

                students = view_students()

                print("\n==== All Students ====")

                for student in students:
                    print(
                        "ID:", student[0],
                        "| Name:", student[1],
                        "| Phone:", student[2],
                        "| Address:", student[3]
                    )

            elif admin_choice == '4':

                lecturers = view_lecturers()

                print("\n==== All Lecturers ====")

                for lecturer in lecturers:
                    print(
                        "ID:", lecturer[0],
                        "| Name:", lecturer[1],
                        "| Phone:", lecturer[2],
                        "| Address:", lecturer[3]
                    )


            else:

                print("Invalid choice.")

        elif choice == '4':

            print("Goodbye!")
            break

        else:

            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()