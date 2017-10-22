from board import Board
from player import Player

board = Board()

board.display()

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
        print ("sup")
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
