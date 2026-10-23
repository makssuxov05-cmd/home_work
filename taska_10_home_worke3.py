first, second = map(int, input('Введите 2 числа через пробел: ').split())


def make_operator(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '**'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        else:
            operation = '/'
        return func(first, second, operation)
    return wrapper


@make_operator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        # Добавляем проверку на деление на ноль, это хорошая практика
        if second == 0:
            return "Ошибка: деление на ноль!"
        return first / second
    elif operation == '*':
        return first * second


result = calc(first, second)
print(f"Результат: {result}")
