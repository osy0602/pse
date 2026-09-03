import sqlite3


def create_connection():
    return sqlite3.connect("college.db")


def create_student_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            address TEXT
        )
    ''')

    conn.commit()
    conn.close()


def create_lecturer_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lecturer (
            lecturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            address TEXT
        )
    ''')

    conn.commit()
    conn.close()


def create_course_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Course (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            time TEXT NOT NULL,
            lecturer_id INTEGER,
            FOREIGN KEY (lecturer_id)
                REFERENCES Lecturer(lecturer_id)
        )
    ''')

    conn.commit()
    conn.close()


def create_enrollment_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Enrollment (
            enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            FOREIGN KEY (student_id)
                REFERENCES Student(student_id),
            FOREIGN KEY (course_id)
                REFERENCES Course(course_id)
        )
    ''')

    conn.commit()
    conn.close()


def create_tables():
    create_student_table()
    create_lecturer_table()
    create_course_table()
    create_enrollment_table()