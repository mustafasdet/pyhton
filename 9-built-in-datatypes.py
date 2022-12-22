""" multiple-line comments
Built-in data types: Python’s yer alan, baska yerden import etmeye gerek olmayan yapilardir.
Python has 4 built-in data types.
- List
- Tuple
- Dictionary
- Set
"""

# List
# - sequential with indexes.
# - Lists are dynamic. It can be increased later. No need to specify such as arrays in Java.
# - heterogenous. Any objects can be elements of a List
# - Elements can be changed, deleted or new elements can be added.

prices = []
temps = [32.0, 212.0, 0.0, 81.6, 100.0, 45.3]
words = ['hello', 'world']
car_details = ['', '', 2.2, 60807]

allLists = [prices, temps, words, car_details]

odds_and_ends = [[1, 2, 3], ['a', 'b', 'c'], ['one', 22, 333]]

print(allLists)
print(odds_and_ends)

print(allLists[1])
print(allLists[0], '\n', allLists[3], '\n', odds_and_ends[2])
