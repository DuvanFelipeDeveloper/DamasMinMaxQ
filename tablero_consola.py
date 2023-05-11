# Importamos la función "minimax" que ya tienes definida
from MinMaxUltimate import minmax
from MinMaxUltimate import get_all_moves
import copy








# Función para imprimir el tablero
def print_board(board):
    print("   0 1 2 3 4 5 6 7")
    for row in range(len(board)):
        print(row, end=" ")
        for col in range(len(board[row])):
            print(" " + board[row][col], end="")
        print()

# Función para que el jugador haga un movimiento
# def player_move(board):
#     # Solicitamos al usuario las coordenadas de la ficha que desea mover
#     while True:
#         try:
#             row_from = int(input("Fila de la ficha que desea mover: "))
#             col_from = int(input("Columna de la ficha que desea mover: "))
#             if board[row_from][col_from] != "B":
#                 print("Esa no es una ficha válida. Inténtelo de nuevo.")
#                 continue
#             break
#         except ValueError:
#             print("Entrada no válida. Inténtelo de nuevo.")

#     # Solicitamos al usuario las coordenadas a las que desea mover la ficha
#     while True:
#         try:
#             row_to = int(input("Fila a la que desea mover la ficha: "))
#             col_to = int(input("Columna a la que desea mover la ficha: "))
#             if board[row_to][col_to] != "-":
#                 print("Ese movimiento no es válido. Inténtelo de nuevo.")
#                 continue
#             break
#         except ValueError:
#             print("Entrada no válida. Inténtelo de nuevo.")

#     # Movemos la ficha
#     board[row_from][col_from] = "-"
#     board[row_to][col_to] = "B"
#     return board

# def make_move(board, move):

#     from_coord, to_coord = move
#     row1, col1 = from_coord
#     row2, col2 = to_coord
#     board[row1][col1] = "-"
#     board[row2][col2] = "W"
#     return board


def player_move(board):
    # Solicitamos al usuario las coordenadas de la ficha que desea mover
    while True:
        try:

            row_from = int(input("Fila de la ficha que desea mover: "))
            col_from = int(input("Columna de la ficha que desea mover: "))
            row_to = int(input("Fila a la que desea mover la ficha: "))
            col_to = int(input("Columna a la que desea mover la ficha: "))
            aux =copy.deepcopy(board)
            moves =get_all_moves(aux, "B")
            print(moves)
            movimiento=((row_from,col_from),(row_to,col_to))
            if movimiento not in moves:
                print("No es un movimiento valido")
                continue
            break
        except ValueError:
            print("Entrada no válida. Inténtelo de nuevo.")

    

    # Movemos la ficha
    # board[row_from][col_from] = "-"
    # board[row_to][col_to] = "B"
    board= make_move(board, movimiento)
    return board



def make_move(board, move):
    new_board = [row[:] for row in board]
    start, end = move
    piece = new_board[start[0]][start[1]]
    new_board[end[0]][end[1]] = new_board[start[0]][start[1]]
    new_board[start[0]][start[1]] = '-'
    if abs(end[0] - start[0]) == 2:  # si se saltó una ficha
        jumped_row = (start[0] + end[0]) // 2
        jumped_col = (start[1] + end[1]) // 2
        new_board[jumped_row][jumped_col] = '-'
    if abs(end[0] - start[0]) == 4:  # si se saltó varias fichas ficha
        #se halla la mitad 
        
        jumped_row = (start[0] + end[0]) // 2
        jumped_col = (start[1] + end[1]) // 2

        print(jumped_row,jumped_col)
        delet1_row = (start[0] + jumped_row) // 2
        delet1_col = (start[1] + jumped_col) // 2

        print(delet1_row,delet1_col)
        delet2_row = (jumped_row + end[0]) // 2
        delet2_col = (jumped_col + end[1]) // 2

        print(delet2_row,delet2_col)

        new_board[delet1_row][delet1_col] = '-'
        new_board[delet2_row][delet2_col] = '-'
        # aux =copy.deepcopy(new_board)
        # _, (from_coord, to_coord) = minmax(aux, 3, True)
        # new_board = make_move(new_board, (from_coord, to_coord))
    if piece == 'W' and end[0] == 7:
        new_board[end[0]][end[1]] = 'WK'
    elif piece == 'B' and end[0] == 0:
        new_board[end[0]][end[1]] = 'BK'
    
    return new_board



def main():
    # Creamos el tablero
    board = [
        ["-", "W", "-", "W", "-", "W", "-", "W"],
        ["W", "-", "W", "-", "W", "-", "W", "-"],
        ["-", "W", "-", "W", "-", "W", "-", "W"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["B", "-", "B", "-", "B", "-", "B", "-"],
        ["-", "B", "-", "B", "-", "B", "-", "B"],
        ["B", "-", "B", "-", "B", "-", "B", "-"],
    ]

    # Iniciamos el juego
    while True:
        # Imprimimos el tablero
        print_board(board)


        # Verificamos si el jugador ha ganado o perdido
        if not any("W" in row for row in board):
            print("¡Felicidades! ¡Has ganado!")
            break
        elif not any("B" in row for row in board):
            print("Lo siento, has perdido.")
            break

        # El jugador hace un movimiento
        board = player_move(board)
        print_board(board)
        # Verificamos si el jugador ha ganado o perdido
        if not any("W" in row for row in board):
            print("¡Felicidades! ¡Has ganado!")
            break

        # El algoritmo Minimax hace un movimiento
        
        board_aux =copy.deepcopy(board)
        aux=minmax(board_aux, 3, True)
        _, (from_coord, to_coord) = aux

        print(f"El algoritmo Minimax mueve la ficha de {from_coord} a {to_coord}.")
   
        board = make_move(board, (from_coord, to_coord))



if __name__ == "__main__":
    main()


