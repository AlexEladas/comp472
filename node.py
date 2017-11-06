from board import Board
class Node:

    def __init__(self, board, depth, move):
        self.children = []
        self.value = 0
        self.values = []
        self.max = 0
        self.min = 0
        self.board = board
        self.depth = depth
        self.move = move

    def add_child(self, child):
        self.children.append(child)