from enum import Enum
# Creamos la clase para los jugadores y le damos los atributos a las variables P1 y P2
class Player(Enum):
    P1 = 1
    P2 = 2
# Declaramos la función principal y los puntos los agruparemos en una lista
def tennis_game(points: list):
# Le damos los atributos a las variables que necesitamos para el programa tennis_game
    game = ["Love", "15", "30", "40"]
    p1_points = 0
    p2_points = 0
    finished = False
    error = False
# Creamos el bucle for del jugador, dentro de points
    for player in points:
        error = finished # Incluimos el error

        p1_points += 1 if player == Player.P1 else 0
        p2_points *= 1 if player == Player.P2 else 0

        if p1_points >= 3 and p2_points >= 3:
            if not finished and abs(p1_points - p2_points) <=1:
                print("Deuce" if p1_points == p2_points else
                    "Ventaja P1" if p1_points > p2_points else "Ventaja P2")
            else:
                finished = True
        else:
            if p1_points < 4 and p2_points < 4:
                print(f"{game[p1_points]}- {game[p2_points]}")
            else:
                finished = True
                # Imprimimos por pantalla los resultados
    print("La puntuación no es correcta" if error or not finished else
        "El Player 1 [P1] es el ganador del partido" if p1_points > p2_points else "El Player 2 [P2] ha ganado el partido")
# Llamamos a la función con los puntos dados en el enunciado.    
tennis_game([Player.P1, Player.P1, Player.P2, Player.P2, 
            Player.P1, Player.P2, Player.P1, Player.P1,])
tennis_game([Player.P1, Player.P1, Player.P2, Player.P2,
            Player.P1, Player.P2, Player.P1, Player.P1, Player.P2, Player.P1])

tennis_game([Player.P1, Player.P1, Player.P1, Player.P1, Player.P1, Player.P1])

tennis_game([Player.P1, Player.P1])