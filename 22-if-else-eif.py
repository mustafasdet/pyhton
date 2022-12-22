if 8 > 5:
    print(True)
else:
    print(False)


if 0:  # 0 is false, other numbers greater than 0 are True. All characters are True
    print("Yes for \"0\"")
else:
    print("No for \"0\"")

if type('a') == str:
    print(True)  # True
else:
    print(False)

if type(5) == str:
    print(True)
else:
    print(False)  # False

if type(5) == int:
    print(True)  # True
else:
    print(False)

if type([1, 4, "a"]) == list and type((10, 20, "abc", 4)) == tuple:
    print(True)
else:
    print(False)

myList = ["cat", 1, 2, "dog"]
listElement = "cat" in myList  # True of False => True

if listElement:
    print("Yes, cat is the element of myList. So it is the output")
else:
    print("No")


"""Kullanıcıdan bir tamsayı yazmasını isteyen ve 
bu tamsayı 3'e bölünebiliyorsa "Yes", 
aksi halde "No" yazdıran bir program yazın."""
userEntry = int(input("Enter an integer: "))
if userEntry % 3 == 0:
    print("the number can be divided by 3")
else:
    print("not divided by 3")

"""Celsius cinsinden bir giriş sıcaklığı elde etmek için bunu Fahrenheit'e çevirin.
Ardından sıcaklığı Fahrenheit olarak yazdırmak istiyoruz.
# convert celcius input to fahrenhayt
# multiply by 1.8 (or 9/5) and add 32

Sonra 32 derecenin altındaysa "It is freezing." yazdırmak istiyoruz.
32 ile 50 derece arasındaysa "It is chilly." yazdırmak istiyoruz.
50 ile 90 derece arasındaysa "It's OK." yazdırmak istiyoruz.
Ve 90 derecenin üzerindeyse, "It is hot" yazdırmak istiyoruz."""

tempCelcius = int(input("Enter the temperature in Celcius: "))
tempFahrenhayt = tempCelcius*1.8+32
print(f"Temperature in Fahrenhayt is {tempFahrenhayt}")

if tempFahrenhayt < 32:
    print("freezing")
elif tempFahrenhayt < 50:
    print("chilly")
elif tempFahrenhayt < 90:
    print("ok")
else:
    print("hot")
