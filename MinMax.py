

def minmax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_game_over(board):
        return evaluate(board), None

    if maximizing_player:
        best_move = None
        for move in get_all_moves_ordered(board, "B"):
            new_board = make_move(board, move)
            eval = minmax(new_board, depth-1, alpha, beta, False)[0]
            if eval > alpha:
                alpha = eval
                best_move = move
            if alpha >= beta:
                break
        return alpha, best_move
    else:
        best_move = None
        for move in get_all_moves_ordered(board, "W"):
            new_board = make_move(board, move)
            eval = minmax(new_board, depth-1, alpha, beta, True)[0]
            if eval < beta:
                beta = eval
                best_move = move
            if alpha >= beta:
                break
        return beta, best_move





def make_move(board, move):
    # print("------------------")
    # print(move)
    # print_board(board)
    
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

        if abs(end[1] - start[1]) == 0:
            num = ()
            if piece == 'B':
                num = ((1, -1), (-1, -1), (1, 1), (-1, 1))
            else:
                num = ((-1, -1), (1, -1), (-1, 1), (1, 1))

            for i in range(2):
                end_x = end[0] + num[i*2][0]
                end_y = end[1] + num[i*2][1]
                start_x = start[0] + num[i*2+1][0]
                start_y = start[1] + num[i*2+1][1]
                if end_x >= 0 and end_x <= 7 and end_y >= 0 and end_y <= 7 and start_x >= 0 and start_x <= 7 and start_y >= 0 and start_y <= 7:
                    end_piece = new_board[end_x][end_y]
                    start_piece = new_board[start_x][start_y]
                    if end_piece != piece and end_piece != '-' and start_piece != piece and start_piece != '-':
                        new_board[end_x][end_y] = '-'
                        new_board[start_x][start_y] = '-'
    
        else :

            jumped_row = (start[0] + end[0]) // 2
            jumped_col = (start[1] + end[1]) // 2


            delet1_row = (start[0] + jumped_row) // 2
            delet1_col = (start[1] + jumped_col) // 2

            delet2_row = (jumped_row + end[0]) // 2
            delet2_col = (jumped_col + end[1]) // 2


            new_board[delet1_row][delet1_col] = '-'
            new_board[delet2_row][delet2_col] = '-'
       
    if piece == 'W' and end[0] == 7:
        new_board[end[0]][end[1]] = 'WK'
    elif piece == 'B' and end[0] == 0:
        new_board[end[0]][end[1]] = 'BK'
    # print_board(new_board)
    return new_board

def print_board(board):
    print("   0 1 2 3 4 5 6 7")
    for row in range(len(board)):
        print(row, end=" ")
        for col in range(len(board[row])):
            print(" " + board[row][col], end="")
        print()




def is_game_over(board):
    # Verificar si hay piezas del jugador negro o del jugador blanco en el tablero
    black_count = count_pieces(board, 'B')
    white_count = count_pieces(board, 'W')
    black_count += count_pieces(board, 'BK')
    white_count += count_pieces(board, 'WK')
    if black_count == 0 or white_count == 0:
        return True

    # Verificar si alguno de los jugadores no tiene movimientos posibles
    black_moves = get_all_moves(board, 'B')
    white_moves = get_all_moves(board, 'W')
    if len(black_moves) == 0 or len(white_moves) == 0:
        return True

    # Si no se cumple ninguna de las condiciones anteriores, el juego no ha terminado
    return False




def evaluate(board):

    white_count = count_pieces(board, 'B')
    black_count = count_pieces(board, 'W')
    white_count += count_pieces(board, 'BK')
    black_count += count_pieces(board, 'WK')
    if black_count == 0:
        return float('inf')  
    elif white_count == 0:
        return float('-inf')  
    else:
        return white_count / (white_count + black_count)

def count_pieces(board, color):
    count = 0
    for row in board:
        for piece in row:
            if piece == color or piece == color.upper():
                count += 1
    return count

def get_all_moves_ordered(board, player):
    moves = get_all_moves(board, player)
    ordered_moves = sorted(moves, key=heuristic_function)
    return ordered_moves

def heuristic_function(move):
    # Esta heurística valora las piezas según su posición en el tablero
    board_size = len(move[0])
    start_x, start_y = move[0]
    end_x, end_y = move[1]
    distance_from_center = abs(board_size / 2 - start_x)
    promotion_bonus = 0
    if end_x == board_size - 1:
        promotion_bonus = 1
    value = distance_from_center + promotion_bonus
    return value

def buscar_parejas_mayor_valor(vector):
    parejas = []
    for tupla in vector:
        diferencia = abs(tupla[0][0] - tupla[1][0])
        parejas.append((tupla, diferencia))
    parejas.sort(key=lambda x: x[1], reverse=True)
    max_dif = parejas[0][1]
    return [x[0] for x in parejas if x[1] == max_dif]

def buscar_parejas_menor_valor(vector):
    parejas = []
    diferencia_minima = float('-inf')
    for pareja in vector:
        diferencia = abs(pareja[0][0] - pareja[1][0])
     
    
        if diferencia > diferencia_minima:
            diferencia_minima = diferencia
            parejas = [pareja]
        elif diferencia == diferencia_minima:
            parejas.append(pareja)
    return parejas


    

def get_all_moves(board, player):
    moves = []
    movesK =[]
    for row in range(8):
        for col in range(8):
            if board[row][col] == player:
                if player == 'W':
                    directions = [(1, -1), (1, 1)]
                else:
                    directions = [(-1, -1), (-1, 1)]
                for direction in directions:
                    row_move, col_move = direction
                    new_row, new_col = row + row_move, col + col_move
                    if 0 <= new_row < 8 and 0 <= new_col < 8:
                        if board[new_row][new_col] == '-':
                            moves.append(((row, col), (new_row, new_col)))
                   
                        elif board[new_row][new_col] != player:
                            jump_row, jump_col = new_row + row_move, new_col + col_move
                            if 0 <= jump_row < 8 and 0 <= jump_col < 8 and board[jump_row][jump_col] == '-':
                                moves.append(((row, col), (jump_row, jump_col)))


                                jump_row2, jump_col2 = jump_row + row_move, jump_col + col_move

                 
                                if  0 <= jump_row2 < 8 and 0 <= jump_col2 < 8 and board[jump_row2][jump_col2] != player  and board[jump_row2][jump_col2] != '-':
                                    x, y = jump_row2 + row_move, jump_col2 + col_move
                                    
                                    if 0 <= x < 8 and 0 <= y < 8 and board[x][y] == '-':
                                        moves.append(((row, col), (x, y)))
                                    
                          
                                if  0 <= jump_row2 < 8 and 0 <= jump_col2-2 < 8 and board[jump_row2][jump_col2-2] != player and board[jump_row2][jump_col2-2] !='-':
                                    x, y = jump_row2 + row_move, jump_col2-2 + col_move
                                    if 0 <= x < 8 and 0 <= y-2 < 8 and board[x][y-2] == '-':
                                        moves.append(((row, col), (x, y-2)))
                                
                                if  0 <= jump_row2 < 8 and 0 <= jump_col2+2 < 8 and board[jump_row2][jump_col2+2] != player and board[jump_row2][jump_col2+2] !='-':
                                    x, y = jump_row2 + row_move, jump_col2+2 + col_move
                                    if 0 <= x < 8 and 0 <= y+2 < 8 and board[x][y+2] == '-':
                                       moves.append(((row, col), (x, y+2)))
            
            elif board[row][col] == player+'K':
                direccionglobal = [[(-1, -1), (-1, 1)], [(1, -1), (1, 1)]]
                for direccions in direccionglobal:

                    for direction in direccions:

                        row_move, col_move = direction
                        new_row, new_col = row + row_move, col + col_move
                        if 0 <= new_row < 8 and 0 <= new_col < 8:
                            if board[new_row][new_col] == '-':
                                movesK.append(((row, col), (new_row, new_col)))
                    
                            elif board[new_row][new_col] != player:
                                jump_row, jump_col = new_row + row_move, new_col + col_move
                                if 0 <= jump_row < 8 and 0 <= jump_col < 8 and board[jump_row][jump_col] == '-':
                                    movesK.append(((row, col), (jump_row, jump_col)))


                                    jump_row2, jump_col2 = jump_row + row_move, jump_col + col_move

                    
                                    if  0 <= jump_row2 < 8 and 0 <= jump_col2 < 8 and board[jump_row2][jump_col2] != player  and board[jump_row2][jump_col2] != '-':
                                        x, y = jump_row2 + row_move, jump_col2 + col_move
                                        
                                        if 0 <= x < 8 and 0 <= y < 8 and board[x][y] == '-':
                                            movesK.append(((row, col), (x, y)))
                                        
                            
                                    if  0 <= jump_row2 < 8 and 0 <= jump_col2-2 < 8 and board[jump_row2][jump_col2-2] != player and board[jump_row2][jump_col2-2] !='-':
                                        x, y = jump_row2 + row_move, jump_col2-2 + col_move
                                        if 0 <= x < 8 and 0 <= y-2 < 8 and board[x][y-2] == '-':
                                            movesK.append(((row, col), (x, y-2)))
                                    
                                    if  0 <= jump_row2 < 8 and 0 <= jump_col2+2 < 8 and board[jump_row2][jump_col2+2] != player and board[jump_row2][jump_col2+2] !='-':
                                        x, y = jump_row2 + row_move, jump_col2+2 + col_move
                                        if 0 <= x < 8 and 0 <= y+2 < 8 and board[x][y+2] == '-':
                                            movesK.append(((row, col), (x, y+2)))
                         

  

    
    if len(moves) > 0 and player == 'B' : 
        mov = buscar_parejas_mayor_valor(moves) 

        if not movesK:
            mov += movesK

        return(mov)                           
       
    if len(moves) > 0 and player == 'W' : 
        mov = buscar_parejas_menor_valor(moves) 
 
        if not movesK:
            mov += movesK

        return(mov)                            
      

    return moves



def Board():
    board = []
    num_rows = 8
    num_cols = 8

    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            if i < 3 and (i + j) % 2 == 1:
                row.append("W")
            elif i > 4 and (i + j) % 2 == 1:
                row.append("B")
            else:
                row.append("-")
        board.append(row)

    return board



# board = [
#     ["-", "W", "-", "W", "-", "W", "-", "W"],
#     ["W", "-", "W", "-", "W", "-", "W", "-"],
#     ["-", "W", "-", "W", "-", "W", "-", "W"],
#     ["-", "-", "-", "-", "-", "-", "-", "-"],
#     ["-", "-", "-", "-", "-", "B", "-", "-"],
#     ["B", "-", "B", "-", "-", "-", "B", "-"],
#     ["-", "B", "-", "B", "-", "B", "-", "B"],
#     ["B", "-", "B", "-", "B", "-", "B", "-"]
# ]

# depth = 2
# evaluation, move = minmax(board, depth, True)

# print("La mejor evaluación es:", evaluation)
# print("La mejor jugada es:", move)

