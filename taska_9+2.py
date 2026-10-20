import datetime
time_now = datetime.datetime.now()

print(time_now)
print(time_now.hour)
print(time_now.year)
print(time_now.timestamp())


my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list2 = []
for x in my_list2:
    if x % 2 == 0:
        new_list2.append(x)

print(new_list2 )



my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
new_list1 = filter(is_even, my_list1)
print(list(new_list1))


my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def is_even(x):
    if x % 2 == 0:
        return True
    return False
new_list1 = filter(is_even, my_list1)
print(list(new_list1))



my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def is_even(x):
    return x % 2 == 0
new_list1 = filter(is_even, my_list1)
print(list(new_list1))


my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list1 = filter(lambda x: x % 2 == 0, my_list1)
print(list(new_list1))
