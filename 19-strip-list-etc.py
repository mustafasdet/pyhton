birthday = "    Happy birthday to you!!!    "
wordStrip = birthday.strip()
print(wordStrip)  # Happy birthday to you!!!
wordRStrip = birthday.rstrip()
print(wordRStrip)  # Happy birthday to you!!!

print(birthday.title())  # Happy Birthday To You!!!
print(birthday.upper())  # HAPPY BIRTHDAY TO YOU!!!


liste3 = list('birthday')
print(liste3)  # ['b', 'i', 'r', 't', 'h', 'd', 'a', 'y']

liste3.sort()
print(liste3)  # ['a', 'b', 'd', 'h', 'i', 'r', 't', 'y']

del liste3[0], liste3[0]  # deletes the first 2 elements
print(liste3)  # ['d', 'h', 'i', 'r', 't', 'y']

del liste3[2:4]  # deletes index 2 and 3
print(liste3)  # ['d', 'h', 't', 'y']

liste3.remove('d')  # removes exact elemet itself.
print(liste3)

liste3.pop()  # deletes from the end
print(liste3)

liste3.clear()  # clears the whole list
print(liste3)  # []

liste3 = list('birthdayyyyy')
liste3.reverse()
print(liste3)

liste4 = [1, 4, 7, 9, 23, 5]
liste4.sort()
print(liste4)

liste4.sort(reverse=True)
print(liste4)
