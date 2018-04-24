#def request():
 #   a = str(input('Input value 1: '))
  #  b = str(input('Input value 2: '))
   # return a+b
#print(request())


c = 1
try:
    while c != 0:
        b = float(input("Input value: "))
        a = c * b
        c = a
        print (c)
except (ValueError):
    print('try again and type only digitss')

else:
    print("oooops, the b type is zero")