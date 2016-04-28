from AIMA.games import *
from Games.ConnectFour import ConnectFour

from Games.heuristic import *

game = ConnectFour()
state = game.initial

turn = 'maquina'
problem_player = 'X'

while True:
    print "Quien empieza?"
    print "1 --> maquina"
    print "2 --> humano"
    input = raw_input()
    if input == "2":
        turn = 'humano'
        problem_player = 'O'
        break
    elif input == "1":
        break

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if turn == 'humano':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]

        state = game.make_move((x, y), state)
        turn = 'maquina'
    else:
        print "Thinking..."
        move = alphabeta_search(state, game, eval_fn=combinedHeuristic, problem_player=problem_player)

        state = game.make_move(move, state)
        turn = 'humano'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
