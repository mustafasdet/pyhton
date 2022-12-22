# Functions/methods are similar as "methods" in Java
# If the function is in a class, it is called "method" in Java
# reusability : we can reuse the function whenever necessary
# maintainability : codes become easier and faster to maintain, fix
# readability : codes become easier to read
# decreases the mistakes with already used and proven functions
#
# def (arg1, arg2)==>  define (argument1, argument2). arguments are optional
# return : the return of a function if there is. optional

def getSum(arg1, arg2):
    sum = arg1 + arg2
    print(sum)
    return sum


arg1 = int(input('Enter the first argument: '))
arg2 = int(input('Enter the second argument: '))
sum1 = getSum(arg1, arg2)


def getSumFromUser():
    input1 = int(input('Enter 1st num: '))
    input2 = int(input('Enter 2nd num: '))
    print(input1+input2)
    return input1+input2


getSumFromUser()

