import random
import client
import server

keys = server.setup()
print(keys)
print("\n")
m = "Mensagem de teste"
print("Mensagem: "+m)
m = client.encrypt(keys[0],m)
print("Mensagem criptografada: "+m)
m = server.decrypt(keys[1],m)
print("Mensagem revertida: "+m)
print("\n")

