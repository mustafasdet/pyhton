# lambda arguments : expression
myLambda = lambda a : a * 3
print(myLambda(20))

multiply = lambda a,b: a*b
print(multiply(12,3))

def myFunc(n):
    return lambda a : a * n

myDoubler = myFunc(2) # myDoubler = a*2

print(myDoubler(11))