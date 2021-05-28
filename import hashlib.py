import hashlib 
h = hashlib.new('sha256')
senha1 = int(input("Insira sua senha: "))
h.update(b"senha1")
h.hexdigest()

password1 = hashlib.sha256(b"senha1").hexdigest()
input("Insira sua senha: ")