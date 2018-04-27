#import math

#a = int(input('input a: '))
#b = int(input('input b: '))
#c = int(input('inpuc c: '))
#d = int(input('input d: '))
#e = int(input('input e: '))
#f = int(input('input f: '))
#z = [a,b,c,d,e,f]
#y = sum(z)
#print('min =', min(z),'\t''max =', max(z),'\t' 'sum =', sum(z))


import random

def test(z):
    k = int(0)
    while k <= 90:
        y = z[k: k + 10]
        k += 10
        print('String', k//10, y)
z = []
i = 0
while i < 100:
    z.append(random.randint(-1000, 1000))
    i += 1
print('\n', 'original: ')
test(z)
x = z
x.sort()
print('\n', 'modified: ')
test(x)



