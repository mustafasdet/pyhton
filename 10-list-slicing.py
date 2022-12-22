saying = 'Don\'t panic!'
print(saying)
print(type(saying))  # <class 'str'>

letters = list(saying)
print(letters)
print(type(letters))  # <class 'list'>

chars = 'a', 'b', 'c'
print(chars)
print(type(chars))  # <class 'tuple'>

listOfChars = list(chars)
print(listOfChars)
print(type(listOfChars))  # <class 'list'>

# slicing:
# myList[start:stop:step]
# stop is excluded

# step means the pacing of the indexes yani artis degeri => 2'ser, 1'er, 3'er ...
# step is optional, if not specified default value is "1"

# saying stringini ve letters list'inin tum elemanlarini slicing ile yazdiralim:
print(saying[:])  # Don't panic!
# ['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']
print(letters[:])

# saying string'ini 'i' harfine kadar 2'ser atlayarak yazdir
print(saying[:9:2])  # Dntpn

# letters list'ini 'o' dan baslayarak 'i' harfine kadar 3'er atlayarak yazdir
print(letters[1:9:3])  # ['o', 't', 'a']

# letters list'ini 'p' den itibaren yazdir:
print(letters[6:])  # ['p', 'a', 'n', 'i', 'c', '!']

# letters list'ini bosluga kadar '' (exclude) yazdir
print(letters[:5])  # ['D', 'o', 'n', "'", 't']

# letters list'ini tersten 't' harfine kadar yazdir
print(letters[-1:-8:-1])  # ['!', 'c', 'i', 'n', 'a', 'p', ' ']

# letters list'inin tamamini tersten yazdir
print(letters[-1::-1])# ['!', 'c', 'i', 'n', 'a', 'p', ' ', 't', "'", 'n', 'o', 'D']
# or
print(letters[::-1]) #['!', 'c', 'i', 'n', 'a', 'p', ' ', 't', "'", 'n', 'o', 'D']
3