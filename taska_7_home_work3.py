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



strings = [
    'результат операции: 42',
    'результат операции: 54',
    'результат работы программы: 209',
    'результат: 2'
]

def result(numb):
    pos = numb.index(':')
    number = int(numb[pos + 2:])
    print(number + 10)


for s in strings:
    result(s)
