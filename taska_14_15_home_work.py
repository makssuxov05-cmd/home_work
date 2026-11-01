import os
from dotenv import load_dotenv
load_dotenv()
import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd=os.getenv('DB_PASSWORD'),
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute(
    "INSERT INTO students (name, second_name) VALUES (%s, %s)",
    ('Tony', 'Stark')
)
student_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
    ('The Mentalist', student_id)
)

cursor.execute(
    "INSERT INTO subjects (title) VALUES (%s)",
    ('география',)
)
subject_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
    ('урок 2', subject_id)
)
lesson_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
    (5, lesson_id, student_id)
)

db.commit()

cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
print(cursor.fetchone())

cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
print(cursor.fetchone())

cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
print(cursor.fetchone())

cursor.close()
db.close()