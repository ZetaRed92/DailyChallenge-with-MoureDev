# Lo primero es declarar la funcion principal, la llamaremos traducor de leet
def leet_translator(txt):
# Seguidamente, le damos los valores alfanuméricos del abc leet a la variable que llamaremos leet
    leet = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
            "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
            "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
            "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}
    
    leet_txt = ""
# Creamos la condicional, para la palabra dentro del texto
    for word in txt:
        if word.upper() in leet.keys(): # Si la palabra transformada en minúscula para evitar errores, está dentro de la variable leet
            leet_txt += leet[word.upper()] # Entonces el texto en leet es la palabra en minúscula dentro del leet
        else: # En caso contrario
            leet_txt += word # Es igual a la palabra
    
    return leet_txt # La función nos retorna el texto en leet

print(leet_translator ("Leet")) # Primer print de prueba: Leet = 1337
print(leet_translator("Testeando el traductor de leet")) # Segundo print de prueba: Testeando el traductor de leet = 735734 ^/)0 31 7I24)(_)[70I2 )3 1337
print(leet_translator(input("Introduce el texto que quieras traducir: ")))  # En este print introducimos un input. Nos saldrá el mensaje para introducir lo que queramos traducir y nos retornará el resultado.