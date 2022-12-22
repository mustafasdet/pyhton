# write a function: return square of the entry

def squareOf(a):
    return a**2


print(squareOf(6))

""" pozitif bir 'r' sayısını dairenin yarıçapı olarak kabul eden (argument olarak alan) ve dairenin alanını hesaplayıp
döndüren bir fonksiyon yazın. Pi değerini 3.14 olarak kullanın """


def areaOfCircle(r):
    return 3.14*r**2


print(areaOfCircle(2))

# write a function to vowels of a word.
# Lets use "set"

# with annotations:


def getVowels(word: str) -> list:  # word: str) -> list ==> these are annotations
    # returns vowels in a string
    vowelsSet = set('aeiou')
    vowelsOfWord = set(word).intersection(vowelsSet)
    return sorted(vowelsOfWord)


print(getVowels('Mustafa'))


def getVowelsOfUserInput():
    word = input('Enter a word: ')
    vowelsSet = set('aeiou')
    vowelsOfWord = set(word).intersection(vowelsSet)
    return sorted(vowelsOfWord)


print(getVowelsOfUserInput())

print(tuple(getVowelsOfUserInput()))
