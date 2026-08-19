import sqlite3


def create_connection():
    return sqlite3.connect("University.db")


def create_student_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            NID INTEGER PRIMARY KEY AUTOINCREMENT,
            F_name TEXT NOT NULL,
            L_name TEXT NOT NULL,
            B_date TEXT
        )
    ''')

    conn.commit()
    conn.close()


def create_lecturer_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lecturer (
            Lecturer_id INTEGER PRIMARY KEY,
            L_firstname TEXT NOT NULL,
            L_lastname TEXT NOT NULL,
            L_email TEXT NOT NULL,
            L_address TEXT
        )
    ''')

    conn.commit()
    conn.close()


def create_subjects_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Subjects (
            Subject_code INTEGER PRIMARY KEY,
            Subject_unit INTEGER,
            Subject_udsc TEXT
        )
    ''')

    conn.commit()
    conn.close()


def create_lecture_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lecture (
            CC INTEGER PRIMARY KEY,
            Lecture_name TEXT NOT NULL,
            Subject_code INTEGER NOT NULL,
            Lecturer_id INTEGER NOT NULL,
            Date TEXT,
            Time TEXT,
            FOREIGN KEY (Subject_code) REFERENCES Subjects(Subject_code),
            FOREIGN KEY (Lecturer_id) REFERENCES Lecturer(Lecturer_id)
        )
    ''')

    conn.commit()
    conn.close()


def create_enrollment_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Enrollment (
            Enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            Student_code INTEGER NOT NULL,
            CC INTEGER NOT NULL,
            Date_of_enrolment TEXT NOT NULL,
            FOREIGN KEY (Student_code) REFERENCES Student(NID),
            FOREIGN KEY (CC) REFERENCES Lecture(CC)
        )
    ''')

    conn.commit()
    conn.close()


def create_tables():
    create_student_table()
    create_lecturer_table()
    create_subjects_table()
    create_lecture_table()
    create_enrollment_table()