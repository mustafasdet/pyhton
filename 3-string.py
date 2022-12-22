#  no need to specify the data type of a string

s = "hello world"
print(s)  # => hello world
print(len(s))  # len(s) = 11 => 11
print(s[len(s)-1])  # = print(s[10]) => d
print(s[-1])  # => d

# \n= new line => sends the rest of the characters to the new line
print("hello \nworld")
print("\"hello\" world")  # => "hello" world
print('\'hello\' world')  # => 'hello' world

print("hello\tworld")  # \t adds tab => hello    world

print("\\")  # => \
print("\\\\")  # => \\
