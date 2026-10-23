from datetime import datetime


date_string = "Jan 15, 2023 - 12:05:33"
date_obj = datetime.strptime(date_string, "%b %d, %Y - %H:%M:%S")
print(date_obj.strftime("%B"))
print(date_obj.strftime("%d.%m.%Y, %H:%M"))




temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

def day(x):
    if x >= 28:
          return True
    else:
        return False
hoot_temperatures = filter(day, temperatures)
print(list(hoot_temperatures))



temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

def day(x):
    return x >= 28

hoot_temperatures = filter(day, temperatures)
print(list(hoot_temperatures))


hoot_temperatures = list(filter(lambda x: x > 28, temperatures))
print(hoot_temperatures)
print(max(hoot_temperatures))
print(min(hoot_temperatures))
average = sum(hoot_temperatures) / len(hoot_temperatures)
print(round(average, 2))