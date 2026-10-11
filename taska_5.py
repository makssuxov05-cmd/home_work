my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {100, 200, 300, 400, 500}
}
my_dict['dict'][('i am a tuple',)] = 'новое значение'
del my_dict['dict']['a']
my_dict['list'].append(60)
del my_dict['list'][1]
my_dict['set'].add(600)
my_dict['set'].remove(100)

print(my_dict)

