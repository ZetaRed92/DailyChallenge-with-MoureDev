import random

# Creamos la función principal con los atributos que se nos pide en el enunciado.
def password_generator(length=8, capital=False, numbers=False, symbols=False):

# Los caracteres los agrupamos en una lista atribuyendole un rango (Siguiendo la tabla ASCII)
    characters = list(range(97, 123))
# Si la letra está capitalizada, los caracteres se igualan a otro rango de la lista
    if capital:
        characters += list(range(65, 91))
# Exactamente igual, si los caracteres son números, se igualan a otro rango de la lista diferente a los anteriores
    if numbers:
        characters += list(range(48, 58))
# Si la contraseña contiene símbolos, le atribuimos otro rango y además le incorporamos los dos rangos anteriores también
    if symbols:
        characters += list(range(33, 48)) + \
            list(range(58, 65)) + list(range(91, 97))
# Contraseña
    password = ""
# La longitud final de la contraseña debe ser superior a 8 e inferior a 16
    final_length = 8 if length < 8 else 16 if length > 16 else length
# Mientras la longitud de la contraseña sea menor que la longitud final, la contraseña será igual a los caracteres con su función randomizada
    while len(password) < final_length:
        password += chr(random.choice(characters))
# Nos retorna la contraseña
    return password

# Impresión de distintos ejemplos por consola
print(password_generator()) # Print de la función
print(password_generator(length=16)) # Print de una pass con longitud 16
print(password_generator(length=3)) # Print de una pass con solo tres caracteres [ERROR]
print(password_generator(length=24)) # Print de una pass con 24 caracteres [ERROR]
print(password_generator(length=14, capital=True)) # Print de una pass con longitud 14 y letra capitular
print(password_generator(length=14, capital=True, numbers=True)) # Print de una pass con longitud 14, letra capitular y usando números
print(password_generator(length=14, capital=True, numbers=True, symbols=True)) # Print de una pass con longitud 14, letra capitular, uso de números y símbolos
print(password_generator(length=14, capital=True, symbols=True)) # Print de una pass con longitud 14, letra capitular y uso de símbolos