def finish_me(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('finish')
    return wrapper

@finish_me
def example(text):
    print(text)

letters = ['R', 'I', 'C', 'K', '!']

for letter in letters:
    example(letter)
