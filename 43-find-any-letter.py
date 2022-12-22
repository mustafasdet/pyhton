# write a function that finds the given letters in a given text

def findLetters():
    text = input('Enter your text: ')
    letters = input('Enter the letters you want to find: ')
    foundLetters = set(text).intersection(set(letters))
    return sorted(foundLetters)


print(findLetters())

# 2nd way with arguments, annotations and default values:


def findLettersWithArgs(text='my default text', letters='ae') -> set:
    return set(text).intersection(set(letters))


print(findLettersWithArgs("Techproed batch 36", ' eawrg'))

print(findLettersWithArgs())
