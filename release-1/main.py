def hiFunction(name):
    return 'Hi, '+name

def sum(a,b):
    return a+b

def isEven(number):
    if number % 2==0:
        return('true')
    else:
        return('false')

def apples(apple):
    return('i have '+str(apple)+' apples')

def getPower(num):
    return num*num

print(hiFunction('Ivan'))
print(sum(1,3.5))
print(isEven(7))
print(apples(10))
print(getPower(6))