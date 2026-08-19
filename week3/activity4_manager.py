from activity4_database import create_connection
import sqlite3


def add_student(F_name, L_name, B_date):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Student (F_name, L_name, B_date) VALUES (?, ?, ?)",
        (F_name, L_name, B_date)
    )

    conn.commit()
    conn.close()
    print("Student added successfully.")


def add_lecturer(Lecturer_id, L_firstname, L_lastname, L_email, L_address):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """INSERT INTO Lecturer
            (Lecturer_id, L_firstname, L_lastname, L_email, L_address)
            VALUES (?, ?, ?, ?, ?)""",
            (Lecturer_id, L_firstname, L_lastname, L_email, L_address)
        )

        conn.commit()
        print("Lecturer added successfully.")

    except sqlite3.IntegrityError:
        print("Lecturer ID must be unique.")

    conn.close()


def add_subject(Subject_code, Subject_unit, Subject_udsc):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """INSERT INTO Subjects
            (Subject_code, Subject_unit, Subject_udsc)
            VALUES (?, ?, ?)""",
            (Subject_code, Subject_unit, Subject_udsc)
        )

        conn.commit()
        print("Subject added successfully.")

    except sqlite3.IntegrityError:
        print("Subject code must be unique.")

    conn.close()


def add_lecture(CC, Lecture_name, Subject_code, Lecturer_id, Date, Time):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """INSERT INTO Lecture
            (CC, Lecture_name, Subject_code, Lecturer_id, Date, Time)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (CC, Lecture_name, Subject_code, Lecturer_id, Date, Time)
        )

        conn.commit()
        print("Lecture added successfully.")

    except sqlite3.IntegrityError:
        print("Lecture could not be added.")

    conn.close()


def add_enrollment(Student_code, CC, Date_of_enrolment):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO Enrollment
        (Student_code, CC, Date_of_enrolment)
        VALUES (?, ?, ?)""",
        (Student_code, CC, Date_of_enrolment)
    )

    conn.commit()
    conn.close()
    print("Enrollment added successfully.")


# Question 1
# How many students are registered in each course?

def students_per_course():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Subjects.Subject_udsc,
               COUNT(Enrollment.Student_code)
        FROM Subjects
        JOIN Lecture
            ON Subjects.Subject_code = Lecture.Subject_code
        LEFT JOIN Enrollment
            ON Lecture.CC = Enrollment.CC
        GROUP BY Subjects.Subject_code, Subjects.Subject_udsc
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows


# Question 2
# List the names and student IDs of students
# who have enrolled in more than one course.

def students_multiple_courses():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Student.NID,
               Student.F_name,
               Student.L_name
        FROM Student
        JOIN Enrollment
            ON Student.NID = Enrollment.Student_code
        GROUP BY Student.NID, Student.F_name, Student.L_name
        HAVING COUNT(DISTINCT Enrollment.CC) > 1
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows