import hashlib 
h = hashlib.new('sha256')

h.update(b"senhan")
h.hexdigest()

senha1 = b"Kryp10N1938"
senha2 = b"k@ne1939FInGer"
senha3 = b"F@lK1936bEnG@1@"

#hash_number = hashlib.sha256(senhan).hexadigest()

hash_number1 = hashlib.sha256(senha1).hexdigest()
print(hash_number1)
hash_number2 = hashlib.sha256(senha2).hexdigest()
print(hash_number2)
hash_number3 = hashlib.sha256(senha3).hexdigest()
print(hash_number3)

