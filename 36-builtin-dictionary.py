"""Built-in data types: Python’s yer alan, baska yerden import etmeye gerek olmayan yapilardir.
Python has 4 built-in data types.
- List
- Tuple
- Dictionary
- Set

List
- sequential with indexes.
- Lists are dynamic. It can be increased later. No need to specify such as arrays in Java.
- heterogenous. Any objects can be elements of a List
- Elements can be changed, deleted or new elements can be added.
"""
# Dictionary: similar to maps in Java
# - not sequential, no index (unlike Lists)
# - dynamic as Lists
# myDict = {key=value, key2=value2}

person1 = ['name', 'Mustafa', 'age', 33, 'from', 'Adana']

personDict = {
    'name': "Mustafa",
    'age': 33,
    'from': 'Adana',
    'home': 'Istanbul'
}
# every element has a key and a value
# Since no indexing in dictionaries, we use keys to call values or elements
print(personDict['name'])  # Mustafa
print(personDict['age'])  # 33
print(personDict['home'])  # Istanbul

personDict['Language'] = "English"
print(personDict)

personDict['familyName'] = 'Tekin'
print(personDict)
