# her bir eleman farkli data type olabilir
#str, bool, int, None, float
myList = ['hello', 5.6, 137, True, None, "son"]
print(myList)  # ['hello', 5.6, 137, True, None, 'son']
print(myList[0])  # hello
print(myList[-1])  # 'son'
print(myList[-2])  # None

# List yapisinda birden fazla index elemani getirmek
# slicing:
# myList[start:stop:step]
# stop is excluded

# step means the pacing of the indexes yani artis degeri => 2'ser, 1'er, 3'er ...
# step is optional, if not specified default value is "1"

print(myList[1:3])  # [5.6, 137]

# start and stop are also optional. start default is "0", stop default is "last index"
print(myList[:])  # no change ['hello', 5.6, 137, True, None, 'son']

print(myList[1:])  # [5.6, 137, True, None, 'son']

print(myList[::2])  # ['hello', 137, None]

print(myList[::-1])  # ['son', None, True, 137, 5.6, 'hello']
# tersten yazdirir
