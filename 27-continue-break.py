for eachChar in "computer":
    print(eachChar, end='-')

# lets skip second character "p" (continue)
print("----***----")
for eachChar in "computer":
    if eachChar == 'p':
        continue
    print(eachChar, end='-')

# lets not print after 'p' (break)

print("----***----")
for eachChar in "computer":
    if eachChar == 'p':
        break
    print(eachChar, end='-')
    print()

count = 0
for char in "university":
    if char == 'i':
        continue
    else:
        count += 1
print(count)
