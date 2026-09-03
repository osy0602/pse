from college_db import create_connection
import sqlite3


def add_student(name, phone, address):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO Student (name, phone, address)
        VALUES (?, ?, ?)
        """,
        (name, phone, address)
    )

    student_id = cursor.lastrowid

    conn.commit()
    conn.close()

    print("Student added successfully.")
    print("Your student ID is:", student_id)

def student_detail(student_id, name):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM Student
        WHERE student_id = ?
        AND name = ?
        """,
        (student_id, name)
    )

    student = cursor.fetchone()

    conn.close()

    return student

def add_lecturer(name, phone, address):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO Lecturer (name, phone, address)
        VALUES (?, ?, ?)
        """,
        (name, phone, address)
    )

    lecturer_id = cursor.lastrowid

    conn.commit()
    conn.close()

    print("Lecturer added successfully.")
    print("Your lecturer ID is:", lecturer_id)

def lecturer_detail(lecturer_id, name):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM Lecturer
        WHERE lecturer_id = ?
        AND name = ?
        """,
        (lecturer_id, name)
    )

    lecturer = cursor.fetchone()

    conn.close()

    return lecturer

def lecturer_courses(lecturer_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            Course.course_id,
            Course.name,
            Course.location,
            Course.time
        FROM Course
        WHERE Course.lecturer_id = ?
    """, (lecturer_id,))

    courses = cursor.fetchall()

    conn.close()

    return courses

def add_course(name, location, time, lecturer_id):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO Course (name, location, time, lecturer_id)
            VALUES (?, ?, ?, ?)
            """,
            (name, location, time, lecturer_id)
        )

        course_id = cursor.lastrowid

        conn.commit()

        print("Course added successfully.")
        print("Course ID is:", course_id)

    except sqlite3.IntegrityError:
        print("Invalid lecturer ID.")

    conn.close()

def enroll_student(student_id, course_id):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO Enrollment (student_id, course_id)
            VALUES (?, ?)
            """,
            (student_id, course_id)
        )

        conn.commit()

        print("Student enrolled successfully.")

    except sqlite3.IntegrityError:
        print("Invalid student ID or course ID.")

    conn.close()

def student_course(student_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            Course.course_id,
            Course.name,
            Course.location,
            Course.time,
            Lecturer.name
        FROM Enrollment
        JOIN Course
            ON Enrollment.course_id = Course.course_id
        JOIN Lecturer
            ON Course.lecturer_id = Lecturer.lecturer_id
        WHERE Enrollment.student_id = ?
    """, (student_id,))

    courses = cursor.fetchall()

    conn.close()

    return courses

def view_students():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, name, phone, address
        FROM Student
    """)

    students = cursor.fetchall()

    conn.close()

    return students


def view_lecturers():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lecturer_id, name, phone, address
        FROM Lecturer
    """)

    lecturers = cursor.fetchall()

    conn.close()

    return lecturers