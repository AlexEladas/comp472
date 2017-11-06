from board import Board
class Node:

    def __init__(self, board, depth, move):
        self.children = []
        self.value = []
        self.board = board
        self.depth = depth
        self.move = move

    def add_child(self, child):
        self.children.append(child)