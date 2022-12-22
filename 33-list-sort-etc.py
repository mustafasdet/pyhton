listFruits = ["banana", "peach", "apple"]
listNums = [20, 5, 4, 12, 100]

# listA.sort(key=None, reverse=False)
listFruits.sort(key=None, reverse=False)
print(listFruits)

listNums.sort()
print(listNums)  # [4, 5, 12, 20, 100]


# None !!! Becasue sort() does not have a return value!!!
print(listNums.sort(reverse=True))
listX = listNums.sort()
print(listX)  # None !!! Becasue sort() does not have a return value!!!
# and because in programming code is read beginning from right of the equality!!!
# if we want to create a different sorted list. We can do the following:

listA = [90, 85, 70, 76, 87, 55]
listA.sort()
listB = listA  # we make an “assignment” by “=“.
# We do not copy the object
# but indicate that object
# (here indicating the list object [90, 85, 70, 76, 87, 55] via listA and then with new assignment with listB)
print(listB)

listC=listA.copy() # myList.copy() is different than the assignment. We create a new object with copy()


listNums.sort(reverse=True)
print(listNums)  # [100, 20, 12, 5, 4]

# help(list.sort)

listNums.reverse()  # same as listNums.sort(reverse=True)
print(listNums)

help(list.reverse)
