def finish_me(func):

    def wrapper(text):
        func(text)
        print('finish')
    return wrapper


@finish_me
def example(text):
    print(text)



@finish_me
def example1(text):
    print(text)

@finish_me
def example2(text):
    print(text)


@finish_me
def example3(text):
    print(text)

@finish_me
def example4(text):
    print(text)
example('R')
example1('I')
example2('C')
example3('K')



