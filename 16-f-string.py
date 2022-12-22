name = "Mustafa"
surname = "tekin"

print(f"Adamin adi {name}, soyadi ise {surname}")

print(f"Adamin adi \"{name}\", soyadi ise \"{surname}\"dir")

# \ => İkaçış diziniİ deniyor

# alt satira yazsak da ciktimiz tek satirda olmasi icin:
print(f"alt satira gecelimmmmmmmmmmm\
mmmmmmmmmmmmm\
mmmmmmmm")

# alt satira yazdigimizda ciktinin da satir atlamasi icin: uc tirnak kullanilir """"
print(f"""alt satira gecelimmmmmmmmmmm
mmmmmmmmmmmmm
mmmmmmmm""")

# yukaridaki islemi "f" olmadan \n ile de yapabiliriz:
print("alt satira gecelimmmmmmmmmmm \n"
      "mmmmmmmmmmmmm\n"
      "mmmmmmmm")

onlukSayi = 14
print(f"Sayinin binary karsiligi = {onlukSayi:b}")
# Sayinin binary karsiligi = 1110

onlukSayi = 32
print(f"Sayinin binary karsiligi = {onlukSayi:b}")
# Sayinin binary karsiligi = 100000

str = "python"
str.upper()
print(str)  # python

str = str.upper()
print(str)  # PYTHON
