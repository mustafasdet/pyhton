listA = ["a", "b", "c"]
print(listA)

# listA.remove(element) >> removes the specific element
listA.remove("a")
print(listA)

# listA.remove("x") ValueError: list.remove(x): x not in list
# print("can not print listA after the error : "+listA)

# listA.pop() >> removes the last element as default
# listA.pop(1) >> removes the specific index
listA.pop()
listA.pop()
# listA.pop() IndexError: pop from empty list
# print("can not print listA after the error : "+listA)

listA.clear()  # removes all elements, makes the list an emptyList []
