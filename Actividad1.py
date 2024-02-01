from cryptography.fernet import Fernet

claveM=input("ingresa tu token")
fM=Fernet(claveM)
msj = input("ingresa msj encryptado")
msj_decry=fM.decrypt(msj)

print(msj_decry)