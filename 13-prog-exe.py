#ex-1
# # Kullanıcıdan 'x' tamsayısını isteyin
# ve aşağıdaki ifadeyi değerlendirdikten sonra
# y'nin değerini yazdıran bir program yazın:
# y = x^2 - 12x + 11    (x^2 ifadesi x'in karesi anlamına geliyor.)

num = int(input('Enter an integer '))

calc = num*num - 12*num + 11
calc2 = (num-11) * (num-1)

print(calc)
print(calc2)

