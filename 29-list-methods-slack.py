"""
vowels = [ 'a', 'e', 'i', 'o', 'u' ]

word  = "Milliways"

for letter in word :
    if letter in vowels :
        print(letter)

# length ()  objenin eleman sayisini dönduruyor

my_list = [ 'two', 5, ['one', 2 ]  ]

print( len(my_list))

# append() methodu :
# append() methodu bir list'in sonuna eleman eklemek için kullanılır.
# Syntax ;   list.append(elmnt)

my_list = []

my_list.append('a')

my_list.append('e')

my_list.append('i')

my_list.append('o')



if 'u' not in my_list :
    my_list.append('u')

print(my_list)



# append ile birden fazla elemanı listin sonuna ekleyemeyiz:

a = ["apple", "banana", "cherry"]

a.append("Ford", "BMW", 5)
print(a)
# TypeError: list.append() takes exactly one argument 
# Bu şekilde birden fazla eleman eklemeye çalışırsanız hata alırsınız...
# append() argument olarak sadece bir eleman alır.

a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.append(b)

print(a)


a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

for element in b :
    a.append(element)

print(a)

"""
