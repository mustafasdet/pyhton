# Call-by-value and Call-by-reference difference
# int, str ... can not be changed directly.
# and we assign them to a different variable as arg = arg * 2

# Instead python uses the copy of them
# That's why the original value of the variable remains the same but the called obj changed

# list, set and dictionary can be changed directly.
# And we do not assign list, set, dict to another variable (arg.append('more data')),
# so we change the original list, set, dict

# Python uses the reference of the variable.
# That's why when the reference is changed the value is also changed.


# Call-by-value
def double(arg):
    print("Before the multiplying: ", arg)
    arg = arg * 2
    print("After the multiplying: ", arg)


num = 10
double(num)
# Before the multiplying:  10
# After the multiplying:  20

word = "hello"
double(word)
# Before the multiplying:  hello
# After the multiplying:  hellohello

# what is the result for the following
print(num, word)  # 10 hello


# Call-by-reference

def change(arg):
    print("Before the append: ", arg)  # [20, 12, 34]
    # append is a list method, so we will use a list as argument.
    # we did not assign it to another variable. So we change the original list
    arg2 = arg.append("More data")
    print("After the append: ", arg)  # [20, 12, 34, 'More data']

    # Newly assigned list arg2=  None
    print("Newly assigned list arg2= ", arg2)


numbers = [20, 12, 34]
change(numbers)
# Before the append:  [20, 12, 34]
# After the append:  [20, 12, 34, 'More data']

print(numbers)
# [20, 12, 34, 'More data']
