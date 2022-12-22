# positional assignment : arguments are used according to their positions in the function
# Keyword assignment: keywords are used in the function
# Keyword assignment can be very useful when there are many arguments
# and we want to specify the keyword

def assign(arg1, arg2, arg3):
    return arg1, arg2*2, arg3*3


# positional assignment
print(assign(3, 5, 7))

# keyword assignment
print(assign(arg3=7, arg1=3, arg2=5))
