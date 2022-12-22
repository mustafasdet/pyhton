for num in range(1, 11):
    print("Each", num, ">>Please note that space is automatically added among parameters in Python")


# Bir for döngüsü kullanarak
# 1'den 101'e kadar olan tüm çift sayıların toplamını
# ekrana yazdıran bir program yazınız.
sum = 0
for i in range(1, 102):
    if (i % 2 == 0):
        sum += i
print(sum)

# 2nd way

sum2 = 0
for i in range(2, 102, 2):
    sum2 += i
print(sum2)

# print the sum from "1" to the input "n"
num = int(input("enter a number: "))
sum = 0
for i in range(1, num+1):
    sum += i
print(sum)

# get input "n" from the user. Print 10^0 10^1 10^2 10^3
# 1
# 10
# 100
# 1000

n = int(input("Enter the number: "))
# if (n > 0):
#     print(1)
for i in range(0, n+1):
    print(10 ** i)
