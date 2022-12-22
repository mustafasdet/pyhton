""" 
- set is for unique elements.
- similar to "kume" in maths 
- index is random! so index is not used."""
set1 = {3, 4, 4, 4, 1, 1, 1, 6, 6}
print(set1)  # {3,4,1,6}

liste2 = ['ad', True, True, (1, 2, 2, 1), 45, "ad", True, False]
print(liste2) #['ad', True, True, (1, 2, 2, 1), 45, 'ad', True, False]

set2 = set(liste2)
print(set2) # {False, True, (1, 2, 2, 1), 45, 'ad'}

set2.add("mustafa")
set2.add("mustafa")
print(set2) #{False, True, (1, 2, 2, 1), 45, 'ad', 'mustafa'}
