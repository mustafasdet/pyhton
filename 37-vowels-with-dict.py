######### Bir kelimenin içindeki sesli harfleri bulan programdır... #########
# solve the problem with "dictionary" class
vowelsDict = {
    'a': 0,
    'e': 0,
    'i': 0,
}
vowelsDict['o'] = 0
vowelsDict['u'] = 0
print(f"Beginning key values are: {vowelsDict}")


# my way
userWord = input('Enter the word: ')
# for letter in userWord:
#     if letter == 'a':
#         vowelsDict['a'] = vowelsDict['a']+1
#     if letter == 'e':
#         vowelsDict['e'] = vowelsDict['e']+1
#     if letter == 'i':
#         vowelsDict['i'] += 1
#     if letter == 'o':
#         vowelsDict['o'] += 1
#     if letter == 'u':
#         vowelsDict['u'] += 1
# print(vowelsDict)

# ** Iterating over a Dictionary **
 # print only keys!!!
for eachKey in vowelsDict:
    print(eachKey) 

# print both key and value
for eachKey in vowelsDict:
    print(eachKey, ">> mySeparator >> ", vowelsDict[eachKey])
    print(
        f"Number of letter for the key: {eachKey}, in the entered word is ==> {vowelsDict[eachKey]} ")

# Since dictionary does not have indexes. We can use a built-in method to sort them
# sorted(vowelsDict)
for eachKey in sorted(vowelsDict):
    # prints both key and value
    print(
        f"Number of letters {eachKey}, with sorted(dictionary) method is {vowelsDict[eachKey]} ")

# items() method returns both key and value.
for key, value in sorted(vowelsDict.items()):
    print(f"The key {key} in the entered word is {value}")


#  Teacher's solution with iteration

vowelsList = ['a', 'e', 'i', 'o', 'u']
for letter in userWord:
    if letter in vowelsList:
        vowelsDict[letter] = vowelsDict[letter]+1

for key, value in sorted(vowelsDict.items()):
    print(f"The key {key} in the entered word is {value}")

# Dictionary setDefault() method:
defaultDict = {}
for eachLetter in userWord:
    if eachLetter in vowelsList:
        defaultDict.setdefault(eachLetter, 0)
        defaultDict[eachLetter] = defaultDict[eachLetter]+1

for key, value in sorted(defaultDict.items()):
    print(f"The number for the key {key} is {value}")
