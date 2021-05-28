from typing import ByteString


string = "Kryp10N1938"

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
arr2 = bytes(string, 'ascii')

print(arr,'\n')

# actual bytes in the string
for byte in arr:
    print(ByteString, end=' ')
print("\n")
for byte in arr2:
    print(byte, end=' ')


from typing import ByteString



string = "k@ne1939FInGer"

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
arr2 = bytes(string, 'ascii')

print(arr,'\n')

# actual bytes in the string
for byte in arr:
    print(ByteString, end=' ')
print("\n")
for byte in arr2:
    print(byte, end=' ') 


from typing import ByteString


string = "F@IK1936bEnG@1@"

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
arr2 = bytes(string, 'ascii')

print(arr,'\n')

# actual bytes in the string
for byte in arr:
    print(ByteString, end=' ')
print("\n")
for byte in arr2:
    print(byte, end=' ')      