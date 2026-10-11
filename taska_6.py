# задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name)
print(last_name)
print(city)
print(phone)
print(country)

# задание 2
s = "результат операции: 42"
pos = s.index(':')
num = int(s[pos + 2:])
print(num + 10)

d = "результат операции: 514"
pos = d.index(':')
num = int(d[pos + 2:])
print(num + 10)

r = "результат операции: 9"
pos = r.index(':')
num = int(r[pos + 2:])
print(num + 10)


# задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

students_str = ', '.join(students)
subjects_str = ', '.join(subjects)

print("Students " + students_str + " study these subjects: " + subjects_str)