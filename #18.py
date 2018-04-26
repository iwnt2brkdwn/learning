import random
a = input('input int or float: ')
if a == 'int':
    b = int(input('input start of range: '))
    c = int(input('input end of range: '))
    x = random.randrange(b, c)
elif a == 'float':
    x = random.random()
print('Your result is', x)