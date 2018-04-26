import square
z = int(input('Input 3 - round, 2 - triangle, 1 - rectangle: '))
if z == 1:
    a = int(input('input a-side: '))
    b = int(input('input b-side: '))
    print(square.rectangle(a, b))
elif z == 2:
    a = int(input('input base: '))
    h = int(input('input height: '))
    print(square.triangle(a,h))
elif z == 3:
    r = int(input('input radius: '))
    print(square.circle(r))
else:
    print('zhep')