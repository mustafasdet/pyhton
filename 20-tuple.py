"""tuple is immutable. 
tuple is faster 
and covers less memory.
tuple has few methods: count() and index()"""

tuple1 = 1, 3, 14, 4, 6
print(type(tuple1))  # <class 'tuple'>
print(tuple1)
# tuple1[0] = 12 # TypeError: 'tuple' object does not support item assignment
print(tuple1)

tupleList = list(tuple1)
print(tupleList)
