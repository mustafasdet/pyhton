myStr = "university"
# Strings are immutable unlike Lists
# we can not make a direct assignment such as
# myStr[0] = 'K'
# We can use builtin string methods to achieve such results

# <class str> String methods:
# myStr.count(value, start,end) : value is required,
# 	- start and end are optional
# 	- start default value is 0
# 	- end default value is last index
# myStr.count(‘e’, 2,5) counts e starting index 2, till index 4 (end (5) is exclusive)

print(myStr.count('e', 1, 4))  # 0
print(myStr.count('e', 1, 5))  # 1

# slicing as in list
print(myStr[2:13:2])  # iest

# myStr.replace(oldValue, newValue, count)
# 	- oldValue and newValue are required
# 	- count is how many of them should be changed.
#           It is optional. Default is all of the values replaced.

myStr.replace('i', 'w')
print(myStr)  # university
replacedStr = myStr.replace('i', '4')
print(replacedStr)  # un4vers4ty

# myStr.split(separatorValue, maxSplit)
# 	- parameters are optional
# 	- separatorValue default is space
# 	- maxSplit default is -1 means all possible splits
#   - if maxSplit = 2, there will be max 2 splits meaning that string will have 3 elements.

txt = "I love java and python"
print(txt.split())  # ['I', 'love', 'java', 'and', 'python']
print(txt.split('a', 1))  # 2 elements=> ['I love j', 'va and python']

# myStr.capitalize() : corrects a sentence with just the first letter is capitalized
myStr = "i LoVE tReeS"
capitalizedStr = myStr.capitalize()
print(capitalizedStr)  # I love trees
print(myStr.lower())  # i love trees
print(myStr.upper())  # I LOVE TREES


# myStr.find() : finds the first index of the searched value
foundIndex = myStr.find('e')
print(foundIndex)  # 9

# separatorSign.join(iterable) : behaving as if opposite of myStr.split()
# 	- split was splitting from a separator and makes an iterable object “list”
# 	-
# iterable: means objects that can be iterated such as list in a loop.

separatorSign = "/==/"
myList = ["one", "two", "three", "four"]

joinedStr = separatorSign.join(myList)
print(joinedStr)  # one/==/two/==/three/==/four
