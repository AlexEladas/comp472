from board import Board
from player import Player
from ai import AI
from node import Node

print("Choose singleplayer(1) or multiplayer(2)")
game_type = 0
player_choice = 0
while True:
    try:
        game_type = int(input())
        if game_type == 1 or game_type == 2:
            break
        else:
            print("Enter 1 for singleplayer or 2 for multiplayer")
    except ValueError:
        print("Enter 1 for singleplayer or 2 for multiplayer")

board = Board()
print("+:black cell, -:white cell")
board.display()
if game_type == 1:

    AI1 = AI("G","R","max")
    AI2 = AI("R","G","min")
    player1 = Player("R","G")
    player2 = Player("G","R")

    print("You want to play as Red(1) or Green(2)?")
    while True:
        try:
            player_choice = int(input())
            if player_choice == 1 or player_choice == 2:
                break
            else:
                print("Enter 1 for Red Player or 2 for Green Player")
        except ValueError:
            print("Enter 1 for Red Player or 2 for Green Player")

    if player_choice == 1:
        while True:
            AI1.build_tree(board, AI1, player1)
            move = AI1.moves[AI1.evaluation]
            print(move)
            if not board.check_if_valid(move, AI1):
                print("AI ENTERED INVALID MOVE. YOU WIN")
                break
            board.move(move,AI1)

            if board.check_if_attacking_move(move, AI1):
                board.attack(move, AI1)
            print(AI1.evaluation)
            board.display()

            if AI1.number_of_tokens == 0:
                print("Green wins!")
                break

            if board.non_attacking_moves >= 10:
                print("Game is a draw")
                break

            print("Red Player Enter your move")
            move = input()
            while (not board.check_if_valid(move, player1)):
                print("Enter Valid move")
                move = input()
            board.move(move, player1)

            if board.check_if_attacking_move(move, player1):
                board.attack(move, player1)
            board.display()

            if player1.number_of_tokens == 0:
                print("Red wins!")
                break

            if board.non_attacking_moves >= 10:
                print("Game is a draw")
                break

    if player_choice == 2:
        while True:
            print("Green Player enter your move")
            move = input()
            while not board.check_if_valid(move, player2):
                print("Enter Valid move")
                move = input()
            board.move(move, player2)

            if board.check_if_attacking_move(move, player2):
                board.attack(move, player2)
            board.display()

            if player2.number_of_tokens == 0:
                print("Green wins!")
                break

            if board.non_attacking_moves >= 10:
                print("Game is a draw")
                break

            AI2.build_tree(board, AI2, player2)
            move = AI2.moves[AI2.evaluation]
            print(move)
            if not board.check_if_valid(move, AI2):
                print("AI ENTERED INVALID MOVE. YOU WIN")
                break
            board.move(move, AI2)

            if board.check_if_attacking_move(move, AI2):
                board.attack(move, AI2)
            print(AI2.evaluation)
            board.display()

            if AI2.number_of_tokens == 0:
                print("Red wins!")
                break

            if board.non_attacking_moves >= 10:
                print("Game is a draw")
                break

if game_type == 2:

    player1 = Player("G","R")
    player2 = Player("R","G")



    while True:
        print("Green Player enter your move")
        move = input()
        while not board.check_if_valid(move,player1):
            print("Enter Valid move")
            move = input()
        board.move(move, player1)

        if board.check_if_attacking_move(move, player1):
            board.attack(move,player1)
        board.display()

        if player1.number_of_tokens == 0:
            print("Green wins!")
            break

        if board.non_attacking_moves >= 10:
            print("Game is a draw")
            break




        print("Red Player Enter your move")
        move = input()
        while (not board.check_if_valid(move, player2)):
            print("Enter Valid move")
            move = input()
        board.move(move, player2)

        if board.check_if_attacking_move(move, player2):
            board.attack(move, player2)
        board.display()

        if player2.number_of_tokens == 0:
            print("Red wins!")
            break

        if board.non_attacking_moves >= 10:
            print("Game is a draw")
            break
