# list1: myList.append(element): can add only one element
# lis2: myList.extend(element1, element2) : can add multiple elements
# myList.extend(“tech”): since string is considered as a list, it still be added [“t”, “e”,”c”,”h”]

listA = ["apple", "banana", "peach"]
listB = ["grapes", "watermelon", "cherry"]

for eachFruit in listB:
    listA.append(eachFruit)
print(listA)  # ['apple', 'banana', 'peach', 'grapes', 'watermelon', 'cherry']

listA.extend("tech")
# ['apple', 'banana', 'peach', 'grapes', 'watermelon', 'cherry', 't', 'e', 'c', 'h']
print(listA)

# We can not use "extend" stringA.extend(stringB)=> gives "'str' object has no attribute 'extend'"
strA = "ford"
strB = "audi"
# strA.extend(strB)  # AttributeError: 'str' object has no attribute 'extend'

# str1: Instead we can use just "+"
strA = strA+' '+strB
print(strA)

print(listA+listB)
# the result is the same as listA.extend(listB)
# But built-in methods are faster!
# And in some cases it is better to use a list method to make it more clear and work

# list3: insert(index, object)
# we can add an element by specifying index.
# It is like append(). It does not add multiple elements. A list would be one element if added

# listAbc = ['a', 'b', 'c']  # list("abc")
# listXyz = ['x', 'y', 'z']  # list("xyz")
# listInsert = ['k', 'l', 'm']  # list("klm")

listAbc = list("abc")
listXyz = list("xyz")
listInsert = list("klm")
# listAbc.insert(1, listInsert)
# print(listAbc)  # ['a', ['k', 'l', 'm'], 'b', 'c']

indexNum = 2
for letter in listInsert:
    listAbc.insert(indexNum, letter)
    indexNum += 1

print(listAbc)
