number = 10

while True:
    user_input = input('я загадал цифру отгадай ..... ')
    if not user_input.isnumeric():
        print('нужно написать число и угадать(((')
        continue
    # тут добавил от себя проверку что это точно число а не str
    user_input = int(user_input)

    if user_input == number:
        print('она догадливый !')
        break
    else:
        print('не правильно попробуй еще')


