import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
cursor.execute('select * from students ')
data = cursor.fetchall()

# for student in data:
#     print(student['second_name'])



cursor.execute('SELECT * FROM students WHERE id = 53')

data2 = cursor.fetchone()
print(data2)

db.close()






# insert into books  (title,   taken_by_student_id) VALUES ('The Mentalist', 25175)
# insert into subjects   (title) VALUES ('гуография')
# insert into lessons    (title, subject_id) VALUES ('урок 2', 23916)
# insert into marks     (value, lesson_id, student_id) VALUES (5, 77599,23486)
