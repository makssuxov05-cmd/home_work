from traceback import print_tb

numbers = [11, 345, 2, 6, 65, 34]

print(max(numbers))
print(min(numbers))
print(sum(numbers))


a = 1 / 3
print(round(a, 4))

print(abs(4))

print(sorted(numbers))
print(sorted(numbers, reverse = True))

numbers.sort()
print(numbers)


my_list3 = [11, 34, 54, 76, 2]
new_list = []
for x in my_list3:
    new_list.append(x * 2)
print(new_list)




my_list = [11, 34, 54, 76, 2]

def mult(x):
    return x * 2

new_list2 = map(mult, my_list)
print(list(new_list2))


my_list = [11, 34, 54, 76, 2]


new_list2 = map(lambda x: x * 2 , my_list)
print(list(new_list2))

# name, surname = input('name and sirname').split()
# print(f'is name {name}, and {surname}')
#
#
# code, namber = map(int, (input('cade and namver')).split())
# print(f'his {code + 2}, and {namber + 6}')







