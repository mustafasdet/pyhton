# specify if the number is prime number (asal sayi)

num = int(input("Enter a number to be checked if it is prime number: "))
is_it_prime = True
for currentFactr in range(2, num):
    if num % currentFactr == 0:
        is_it_prime = False
        break
print(f"the number {num} is prime number? {is_it_prime}")

# Lets check all the numbers till "n" if it is prime or not?

lastNum = int(input("enter 'n' number to be checked from 1 to n: "))
for currentNum in range(2, lastNum+1):
    is_the_currentNum_prime = True
    for currentFactor in range(2, currentNum):
        if currentNum % currentFactor == 0:
            is_the_currentNum_prime = False
            break
    print(
        f"Inside the inner for loop==> the number currentNum {currentNum} is prime number? {is_the_currentNum_prime}")
    if is_the_currentNum_prime == True:
        print(f"{currentNum} is prime number")
    else:
        print(f"{currentNum} is NOT prime")
print(
    f"the number currentNum {currentNum} is prime number? {is_the_currentNum_prime}")

# 2nd way
ilk_sayi = 2
son_sayi = 50
mevcut_sayi = ilk_sayi
while mevcut_sayi <= son_sayi:
    mevcut_bolen = 2
    mevcut_sayi_asal_mi = True
    while mevcut_bolen < mevcut_sayi:
        if mevcut_sayi % mevcut_bolen == 0:
            mevcut_sayi_asal_mi = False
            break
        mevcut_bolen = mevcut_bolen + 1
    if mevcut_sayi_asal_mi:
        print(mevcut_sayi, " asaldir")
    else:
        print(mevcut_sayi, "asal degildir")
    mevcut_sayi = mevcut_sayi+1
print("Islem bitti.")
