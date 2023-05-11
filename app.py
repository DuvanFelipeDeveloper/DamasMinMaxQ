from flask import Flask, request, jsonify
from flask_cors import CORS
from MinMaxUltimate import get_all_moves 
from MinMaxUltimate import minimaxQ 
from MinMaxUltimate import make_move
import random

from flask_socketio import emit
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import join_room
from MinMax import minmax








app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
socketio = SocketIO(app, cors_allowed_origins="*")

partidas = {}

jugadores = {}

turno = 1

@socketio.on('connect')
def test_connect():
    print('Cliente conectado')

@socketio.on('disconnect')
def test_disconnect():
    print('Cliente desconectado')


@socketio.on('unirse_a_partida')
def unirse_a_partida(codigo_partida):
    # Busca la sala correspondiente al código de partida
    sala = partidas.get(codigo_partida)
    if sala is None:
        # Si no se encuentra una sala, envía un mensaje de error al cliente
        emit('error', {'mensaje': 'El código de partida es inválido'})
    else:
        # Si se encuentra una sala, une al cliente a la sala y envía un mensaje de confirmación
        join_room(sala)
        # Almacena al jugador en la lista de jugadores activos en la sala
        if sala not in jugadores:
            jugadores[sala] = []
        jugadores[sala].append(request.sid)
        emit('partida_unida', {'mensaje': 'Te has unido a la partida ' + codigo_partida}, room=sala)

        # Si es el primer jugador en unirse a la sala, inicia el juego
        if len(jugadores[sala]) == 2:
            global turno
            turno = 1
            # Envía el primer mensaje de turno al jugador 1
            emit('tu_turno', {'mensaje': 'Es tu turno'}, room=jugadores[sala][0])


@socketio.on('crear_partida')
def crear_partida():
    # Genera un código de partida aleatorio
    codigo_partida = str(random.randint(1000, 9999))
    # Crea una nueva sala para la partida
    sala = 'partida_' + codigo_partida
    # Almacena el código de partida y la sala correspondiente en el diccionario de partidas
    partidas[codigo_partida] = sala
    # Une al creador de la partida a la sala y envía el código de partida al cliente
    join_room(sala)
    # Almacena al jugador en la lista de jugadores activos en la sala
    if sala not in jugadores:
        jugadores[sala] = []
    jugadores[sala].append(request.sid)
    emit('partida_creada', {'codigo_partida': codigo_partida}, room=sala)


@socketio.on('realizar_jugada')
def realizar_jugada(data):
    codigo= data['sala']
    sala = partidas.get(codigo)

    selected = data['selected']
    target = data['target']

    print("si esta llegando aca gonorrea")
    # Envía la jugada a todos los jugadores en la sala excepto al que la realizó
    emit('jugada_realizada', {'selected': selected, 'target':target  }, room=sala)
    # Alterna el turno al otro jugador si hay al menos dos jugadores en la sala
    global turno
    if sala in jugadores and len(jugadores[sala]) >= 2:
        turno = 2 if turno == 1 else 1
        # Envía el mensaje de turno al siguiente jugador
        emit('tu_turno', {'mensaje': 'Es tu turno'}, room=jugadores[sala][turno-1])


@app.route('/')
def index():
    return 'Hola, mundo!'



@app.route('/allmoves', methods=['POST'])
def allmoves():
    data = request.json
    my_list = data['board']
    my_string = data['player']
    row = data['row']
    col = data['col']

    initiallocal = (row,col)

    getall = get_all_moves(my_list, my_string)
    moves =[]
    for ubicacion in getall:
        if ubicacion[0] == initiallocal :
            moves.append(ubicacion[1])

    
    return jsonify(moves)


@app.route('/minmaxQ', methods=['POST'])
def minmaxQ():
    moves =[]
    epsilon = 0.1
    data = request.json
    board =data['board']
    depth = data['depth']
    player = "W"
    maximizing_player = data['maximizing_player']
    # aux=minmax(board, depth, float('-inf'), float('inf'), maximizing_player)
    aux= minimaxQ(board, player, depth, float('-inf'), float('inf'), epsilon)
   
    # El objeto aux no es iterable, hacer algo más...
    _, (from_coord, to_coord) = aux
    moves.append(from_coord)
    moves.append(to_coord)
    return jsonify(moves)


@app.route('/minmax', methods=['POST'])
def min():
    moves =[]
    data = request.json
    board =data['board']
    depth = data['depth']
    maximizing_player = data['maximizing_player']
    aux=minmax(board, depth, float('-inf'), float('inf'), maximizing_player)
    _, (from_coord, to_coord) = aux
    moves.append(from_coord)
    moves.append(to_coord)
    return jsonify(moves)



@app.route('/make_move', methods=['POST'])
def make():
    data = request.json
    tablero = data['tablero']
    selected_row, selected_cell = data['selected']
    row_index, cell_index = data['target']

    response = make_move(tablero, ((selected_row, selected_cell), (row_index, cell_index)))

    return jsonify(response)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
