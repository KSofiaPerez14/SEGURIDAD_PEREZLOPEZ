from cryptography.fernet import Fernet

print("mensaje enviado")
llave = Fernet.generate_key()

#Generamos la instancia de Fernet
f=Fernet(llave)

print("Llave", llave)
#Encriptamos el mensaje
token=f.encrypt(b'te quiero marianita')
print("Token",token)


print("mensaje recibido")

claveM=input("Ingresa tu token: ")
fM=Fernet(claveM)
msj = input("Ingresa msj encryptado:")
msj_decry=fM.decrypt(msj)

print(msj_decry)