str = "hello world of          wonders. How are you doing?"
print(type(str))
split1 = str.split()
print(split1)
#['hello', 'world', 'of', 'wonders.', 'How', 'are', 'you', 'doing?']
print(type(split1))  # <class 'list'>

str2 = "Hello!"
split2 = str2.split()
print(split2)  # ['Hello!']
print(type(split2))  # <class 'list'>

list1 = list(str2)
print(list1)  # ['H', 'e', 'l', 'l', 'o', '!']

withSpaces = "  Hello!    "
# bastaki ve sondaki bosluklari trim (strip) yapiyor
stripped = withSpaces.strip()
print(stripped)  # Hello!
