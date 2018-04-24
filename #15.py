#Параметры и аргументы функций


def getInput():
    global a
    a = str(input('Input value: '))
    print('1')
    return a

#print('Your input was',getInput())
#a = input('Input smthng: ')

def testInput(a):
    try:
        global test
        test = int(a)
        print('2')
        return True
    except(ValueError):
        print('-2')
        return False
#
#a = input('Input value: ')
def strToInt():
        if y == True:
            test = int(a)
            print('3')
            return test
        else:
            print('-3')
#print(a)
def printInt():
    print(test)

getInput()
#print(a)
y = bool(testInput(a))
print(y)
strToInt()
printInt()