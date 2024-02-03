import random
import hashlib

# Paso 1: Número primo p y g=2
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9CC80E2AE63277870C43A567383808EABEDE7A5A5087D3838383E692BB97916BCCDCB6AADA1B8CC36B46AA1F0454FB0E779D8E39C6ED2C7AA6D3F55B8C4126766833BC8980F12C24BCC2344C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9CC80E2AE63277870C43A567383808EABEDE7A5A5087D3838383E692BB97916BCCDCB6AADA1B8CC36B46AA1F0454FB0E779D8E39C6ED2C7AA6D3F55B8C41
g = 2

# Paso 2: Generar llaves privadas aleatorias de 256 bits para Alice y Bob
a_private_key = random.getrandbits(256)
b_private_key = random.getrandbits(256)

# Paso 3: Simular el intercambio de números entre Alice y Bob
A = pow(g, a_private_key, p)
B = pow(g, b_private_key, p)

# Paso 4: Calcular la llave secreta "s" y verificar que sean iguales mediante SHA-256
s_alice = pow(B, a_private_key, p)
s_bob = pow(A, b_private_key, p)


#Paso 5 Aplicar hash SHA-256
s_alice_hash = hashlib.sha256(str(s_alice).encode()).hexdigest()
s_bob_hash = hashlib.sha256(str(s_bob).encode()).hexdigest()

# Verificar si las llaves secretas son iguales
if s_alice_hash == s_bob_hash:
    print("Las llaves secretas son iguales:")
    print("Llave secreta Alice:", s_alice_hash)
    print("Llave secreta Bob:", s_bob_hash)
else:
    print("Las llaves secretas no son iguales.")