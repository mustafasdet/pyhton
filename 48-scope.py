def myFunc():
    localVar = 300
    print(localVar)


# print(localVar)# err: Because it can not be called out of the function because it is local

globalVar = 900


def secondFunc():
    print(globalVar)


secondFunc()

# we can change a local variable to global variable:


def changeScope():
    global localToGlobal
    localToGlobal = 300
    print(localToGlobal)


changeScope()  # we call the function then the variable becomes global!!!
print(localToGlobal)
useLocalToGlobal = localToGlobal * 12
print(useLocalToGlobal)
