# Declaramos la función
def fizzbuzz():
    # Determinamos el rango en el bucle for, en este caso para que incluya el nº100 debemos llevarlo hasta el 101
    for num in range (1, 101):
        # Primera condición del bucle: Si el número es múltiplo de 3 y de 5. 
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz") # Imprime por consola fizzbuzz en lugar de los números que cumplan esta condición.
        # Segunda condición del bucle: Si el número es múltiplo de 3.
        elif num % 3 == 0:
            print("fizz") # Imprime por consola fizz en lugar de los números que cumplan esta condición.
        # Tercera condición del bucle: Si el número es múltiplo de 5.
        elif num % 5 == 0:
            print("buzz") # Imprime por consola buzz en lugar de los números que cumplan esta condición.
        else: # Si no cumple ninguna de las condiciones anteriores.
            print(num) # Imprime por consola el número.
fizzbuzz() # Llamado a la función.