import cryptography

keys = cryptography.setup()
print(keys)
print("\n")
m = "Mensagem de teste"
print("Mensagem: "+m)
m = cryptography.encrypt(keys[0],m)
print("Mensagem criptografada: "+m)
m = cryptography.decrypt(keys[1],m)
print("Mensagem revertida: "+m)
print("\n")

