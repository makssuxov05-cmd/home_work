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


print()
print()
print()
print()

a = 'результат операции: 42'

b = 'результат операции: 54'

d = 'результат работы программы: 209'

c = 'результат: 2'


def result(numb):
    pos = numb.index(':')
    number = int(numb[pos +2:])
    print(number + 10)

result(a)
result(b)
result(d)
result(c)