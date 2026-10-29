import requests
from datetime import datetime, timedelta


url = "https://raw.githubusercontent.com/eugene-okulik/qwerty-qa/main/homework/eugene_okulik/hw_13/data.txt"


response = requests.get(url)
response.raise_for_status()


for line in response.text.splitlines():
    if not line.strip():
        continue


    parts = line.split(' - ')
    if len(parts) != 2:
        continue


    left_part = parts[0]
    action_text = parts[1].strip()


    number, date_str = left_part.split('. ', 1)


    date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")


    print(f"\nСтрока {number}:")
    print(f"Исходная дата: {date_str}")

    if "на неделю позже" in action_text:

        new_date = date_obj + timedelta(days=7)
        print(f"Дата на неделю позже: {new_date.strftime('%Y-%m-%d %H:%M:%S.%f')}")

    elif "день недели" in action_text:

        weekdays_ru = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        day_index = date_obj.weekday()
        print(f"День недели: {weekdays_ru[day_index]}")

    elif "сколько дней назад" in action_text:

        now = datetime.now()
        delta = now - date_obj

        print(f"Дней назад: {delta.days}")

    else:
        print(f"Действие не распознано: {action_text}")