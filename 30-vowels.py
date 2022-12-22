######### Bir kelimenin içindeki sesli harfleri bulan programdır... #########
sesliler = ['a', 'e', 'i', 'o', 'u']
kelime = "TechProeducation"
found = []

for harf in kelime:
    if harf in sesliler:
        if harf not in found:
            found.append(harf)

for sesli_harf in found:
    print(sesli_harf, end='-')
# my answer =============
print()
vowels = ['a', 'e', 'i', 'o', 'u']
userEntry = input("Enter a word to find and count vowels : ")
vowelsStr = ""
print(type(vowelsStr))
count = 0
for letter in userEntry:
    if letter in vowels:
        count += 1
        vowelsStr = vowelsStr+' '+letter
print(f"There are {count} vowels in your word: {vowelsStr}")

# another way with using "list"
vowels = ['a', 'e', 'i', 'o', 'u']
userEntry = input("Enter a word to find and count vowels :")
vowelsList = []
userEntryList = list(userEntry)  # converting the userEntry string to a list!!!
print(type(userEntryList))
count = 0
for letter in userEntryList:
    if letter in vowels:
        count += 1
        vowelsList.append(letter)
print(f"There are {count} vowels in your word: {vowelsList}")


# print the unique vowels of a user input
vowels = ['a', 'e', 'i', 'o', 'u']
userEntryList = list(input("We will display unique vowels in your entry: "))

count = 0
uniqueVowelsList = []
uniqueCount = 0
for letter in userEntryList:
    if letter in vowels:
        count += 1
        if letter not in uniqueVowelsList:
            uniqueVowelsList.append(letter)
            uniqueCount += 1

print(f"There are a total of {count} vowels")
print(f"There are {uniqueCount} unique vowels : {uniqueVowelsList}")
