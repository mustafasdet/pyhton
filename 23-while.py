"""
While there are cookies in the plate,
Continue to eat
"""
# 1'den 101'e kadar 5'e bölünebilen sayıların toplamını ekrana yazdıran bir program yazınız.
# ( 1 ve 101 dahildir) (While döngüsü kullanın)

sum = 0
counter = 0
while counter in range(101):
    if counter % 5 == 0:
        sum += counter
    counter = counter+1
print(sum)

# Kullanıcıdan pozitif bir tamsayı olan n yazmasını isteyen ve ardından n'nin faktöriyelini yazdıran
# while döngüsünü kullanan bir program yazın.
# Faktöriyel, 1'den n'ye (1 ve n dahil) kadar tüm sayıların çarpımı olarak tanımlanır.
# Örneğin 4'ün faktöriyeli 24'e eşittir. (çünkü 1*2*3*4=24)

userInput = int(input("Enter factorial: "))
i = 1
result = 1
while i <= userInput:
    result = result*i
    i += 1
print(f"The factorial of the user input {userInput} equals to {result}")


# 1'den 1001'e kadar 3'er artisla sayılarin toplamını (hem 1 hem de 1001 dahildir) yazdıran
#  while döngüsünü kullanan bir program yazın

sum = 0
counter = 1

while counter < 1002:
    sum = sum + counter  # sum+=counter
    counter += 3
print(f"sum = {sum}")
