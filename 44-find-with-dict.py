# write a function that finds the number of the given letters in a given text
def countSpecifiedLetters(text: str, letters: str) -> dict:
    lettersDict = {}
    for eachLetter in text:
        if eachLetter in letters:
            lettersDict.setdefault(eachLetter, 0)
            # lettersDict[eachLetter]=lettersDict[eachLetter]+1
            lettersDict[eachLetter] += 1
    return lettersDict


print(countSpecifiedLetters('Mustafa Tekin', 'ak'))
