import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

try:
    longitud = int(input("Introduce la longitud de la contraseña: "))

    password = ""

    for i in range(longitud):
        password += random.choice(caracteres)

    print(f"La contraseña generada es: {password}")

except ValueError:
    print("Debes introducir un número entero.")