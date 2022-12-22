# Sets are similar to sets in maths (and sets in Java)
# elements are unique
# No indexes, so no sequence

setA = set('hello adana')
print(setA)  # {'h', 'o', 'l', 'a', 'n', 'e', 'd', ' '}

# sorted(setA) method changes the data type to a list ==>>> []
print(sorted(setA))  # [' ', 'a', 'd', 'e', 'h', 'l', 'n', 'o']
# or same result with following:
sortedSetA = sorted(setA)
print(sortedSetA)  # [' ', 'a', 'd', 'e', 'h', 'l', 'n', 'o']

# union() method: just like "union in Maths"
unionSetA = setA.union(set('hometown: '))
# {' ', 'm', 'd', ':', 'o', 'l', 'a', 'n', 'w', 't', 'e', 'h'}
print(unionSetA)
# [' ', ':', 'a', 'd', 'e', 'h', 'l', 'm', 'n', 'o', 't', 'w']
print(sorted(unionSetA))

# difference() method: "just like difference in Maths"
# in this method the sequence of the sets is very important ==> A-B != B-A
setB = set('bye Konya')
differenceOfSetASetB = setA.difference(setB)
print(differenceOfSetASetB)  # {'h','l','d'}

differenceOfSetB_SetA = setB.difference(setA)
print(differenceOfSetB_SetA)


# intersection() method: just like intersection in Maths
intersectSetASetB = setA.intersection(setB)
print(intersectSetASetB)  # {'o', 'e', ' ', 'n', 'a'}


######### Bir kelimenin içindeki sesli harfleri bulan programdır... #########

# sesliler = ['a', 'e', 'i', 'o', 'u']

# sesliler = set('aeiou')

# kelime = input("Sesli harf aranacak kelimeyi giriniz: ")
# # found = []

# """
# for harf in kelime :
#     if harf in sesliler :
#         if harf not in found :
#             found.append(harf)
# """

# found = sesliler.intersection(set(kelime))
# for sesli_harf in found:
#     print(sesli_harf)

# same exercise ==> find vowels in a given string

userWord = input('Please enter a word: ')
vowelsSet = {'a', 'e', 'i', 'o', 'u'}
setOfVowels = set(userWord).intersection(vowelsSet)

print(
    f"There are '{len(setOfVowels)}' unique vowels and those are ==> {setOfVowels}")
