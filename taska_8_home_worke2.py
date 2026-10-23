def fibonacci_generator():

    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_nth_fibonacci(n):

    count = 1
    for num in fibonacci_generator():
        if count == n:
            return num
        count += 1


# Позиции, которые нужно вывести
positions = [5, 200, 1000, 100_00]

for pos in positions:
    print(f"{pos}-е число Фибоначчи: {get_nth_fibonacci(pos)}")
