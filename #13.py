try:
    x = float(input('1 - боковая площадь, 2 - полная площадь: '))
    r = float(input('Введите радиус: '))
    h = float(input('Введите высоту: '))
    p = 3.14
    s = 0


    def cylinder():
        def circle():
            return int((p * (r ** 2)))

        if x == 1:
            s = 2 * p * r * h
            print('Площадь равна %.2f' % s)
        elif x == 2:
            s =  2 * p * r * h +2 * circle()
            print('Площадь равна %.2f' % s)
except ValueError:
    print('wrong value, must be int or float')
cylinder()