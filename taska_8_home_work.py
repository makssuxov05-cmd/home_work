
import random

salary = input('Введите число: ')
bonus = random.choice([True, False])


if not salary.isnumeric():
    print('Нужно написать число')
    exit()

salary = int(salary)

if bonus == True:
    salary = salary + random.randint(100, 5000)

print(f'${salary}')


# import random
#
# salary = int(input('Введите зарплату: '))
# bonus = random.choice([True, False])
#
# if bonus == True:
#     salary = salary + random.randint(100, 5000)
#
# print(f'${salary}')
