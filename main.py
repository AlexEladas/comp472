from board import Board
from pprint import pprint

board = Board()


for row in board.board:
    for cell in row:
       print(cell.token)


