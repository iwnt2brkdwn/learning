#циклично запрашивает у пользователя номера символов по таблице Unicode и выводит соответствующие им символы

#def loop():
#    try:
#        a = input('Input Unicode: ')
#        a = int(a)
#        return a
#    except (ValueError):
#        print('ti rukozhop')

#g = loop()

#while g != 0:
#    print(chr(g))
#    loop()
#else:
#    print('uve found it')


#g


#Измерение длины, >10 - предупреждение, <10 - добавление символов до 10

#a = input('Input value: ')
#b = len(a)
#if b > 10:
#    print('Warning! Alarm!!!1111')
#elif b < 10:
#    z = 10 - b
#    a = str(a) + z * '*'
#    print(a)


#запрашивает у пользователя шесть вещественных чисел
a = float(input('1: '))
b = float(input('2: '))
c = float(input('3: '))
d = float(input('4: '))
e = float(input('5: '))
f = float(input('6: '))

if a > b and a > c and a > d and a > e and a > f:
    print('max = a')
elif b > a and b > c and b > d and b > e and b > f:
    print('max b')
elif c > a and c > b and c > d and c > e and c > f:
    print('max c')
elif d > a and d > b and d > c and d > e and d > f:
    print('max d')
elif e > a and e > b and e > c and e > d and e > f:
    print('max e')
elif f > a and f > b and f > c and f > d and f > e:
    print('Max f')

if a<b and a < c and a < d and a < e and a < f:
    print('min = a')
elif a < b and c < b and b < d and b < e and b < f:
    print('min b')
elif c < a and c < b and c < d and c < e and c < f:
    print('min c')
elif d < a and d < b and d < c and d < e and d < f:
    print('min d')
elif e < a and e < b and e < c and e < d and e < f:
    print('min e')
elif f < a and f < b and f < c and f < d and f < e:
    print('min f')
