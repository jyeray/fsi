from AIMA.games import *
from ConnectFour.Heuristic.Heuristic import *
from Games.ConnectFour import ConnectFour

game = ConnectFour()
state = game.initial

turn = 'maquina'
problem_player = 'X'
depth = 0

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
    print "Selecciona la dificultad:"
    print "1 --> facil"
    print "2 --> medio"
    print "3 --> dificil"
    difficulty = raw_input()
    if difficulty == "1":
        depth = 2
        break
    elif difficulty == "2":
        depth = 3
        break
    elif difficulty == "3":
        depth = 5
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
        move = alphabeta_search(state, game, eval_fn=combined_heuristic, problem_player=problem_player, d=depth)

        state = game.make_move(move, state)
        turn = 'humano'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
