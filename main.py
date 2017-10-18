from board import Board
from player import Player
from pprint import pprint
import operator
board = Board()

for row in board.board:
    for cell in row:

       print(cell.token)

player1 = Player("G","R")
move = "D5 C5"

if board.check_if_valid(move, player1):
    if board.check_if_attacking_move(move, player1):
        board.move(move,player1)
        board.attack(move,player1)
        print ("sup")
        #print (player1.attack_type)
else:
    print("no sup")

for row in board.board:
    for cell in row:

       print(cell.token)