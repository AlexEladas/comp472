import board as Board
from node import Node
import heuristic as h
import pprint
import copy

class AI:
    MAP = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E"
    }
    def __init__(self, colour, opponent, minmax):
        self.minmax = minmax
        self.colour = colour
        self.attack_type = ""
        self.operationx = ""
        self.operationy = ""
        self.opponent = opponent
        self.number_of_tokens = 22
        self.non_attacking_moves = 0
        self.possible_moves = []
        self.evaluation = 0
        self.moves = {}

    def copy(self, board):
        copy = []
        for i in range(5):
            row = []
            for j in range(9):
                row.append((board[i][j]).copy())
            copy.append(row)
        return copy

    def newevaluate(self, board):
        score = 0
        for i in range(5):
            for j in range(9):
                if board[i][j]['token'] == "G":
                    score += 500
                    moves = h.find_moves(board,i ,j)
                    for move in moves:
                        if not h.check_if_attacking_move(board,move,"G"):
                            score -= 250

                if board[i][j]['token'] == "R":
                    score -= 500
                    moves = h.find_moves(board, i, j)
                    for move in moves:
                        if not h.check_if_attacking_move(board, move, "R"):
                            score += 250
        return score

    def evaluate(self, board):
        score = 0
        for i in range(5):
            for j in range(9):
                if board[i][j]['token'] == "G":
                    score += 500

                if board[i][j]['token'] == "R":
                    score -= 500
        return score

    def build_tree(self, board, ai, opponent):
        tmp_non = Board.non_attacking_moves
        tmpai = ai.number_of_tokens # For resetting at the end of tree. Used for win condition
        tmpop = opponent.number_of_tokens
        future_board = self.copy(board)
        root = Node(future_board,"")

        for move in self.find_possible_moves(future_board,Board, ai.colour):
            future_board = self.copy(board)
            Board.move(future_board, move, ai)
            if Board.check_if_attacking_move(future_board, move, ai):
                Board.attack(future_board, move, ai)
                #Board.display(future_board)

            root.add_child(Node(future_board, move))

        for child in root.children:
            for move in self.find_possible_moves(child.board,Board, ai.opponent):
                future_board = self.copy(child.board)
                Board.move(future_board, move, opponent)
                if Board.check_if_attacking_move(future_board, move, opponent):
                    Board.attack(future_board, move, opponent)
                child.add_child(Node(future_board, move))

        for parent in root.children:
            for child in parent.children:
                for move in self.find_possible_moves(child.board,Board, ai.colour):
                    future_board = self.copy(child.board)
                    Board.move(future_board, move, ai)
                    if Board.check_if_attacking_move(future_board, move, ai):
                        Board.attack(future_board, move, ai)
                    #Board.display()
                    child.add_child(Node(future_board, move))
        ai.number_of_tokens = tmpai
        opponent.number_of_tokens = tmpop
        Board.non_attacking_moves = tmp_non
        self.minimax(root)

    def minimax(self, node):
        print ("supp")
        for grandparent in node.children:
            for parent in grandparent.children:
                for child in parent.children:
                    child.value = self.evaluate(child.board)
                    parent.values.append(child.value)
                try:
                    if self.minmax == "max":
                        parent.value = max(parent.values)
                    if self.minmax == "min":
                        parent.value = min(parent.values)
                except ValueError:
                    parent.value = self.evaluate(parent.board)
                grandparent.values.append(parent.value)
            try:
                if self.minmax == "min":
                    self.moves[max(grandparent.values)] = grandparent.move
                    node.values.append(max(grandparent.values))
                if self.minmax == "max":
                    self.moves[min(grandparent.values)] = grandparent.move
                    node.values.append(min(grandparent.values))
            except ValueError:
                    self.moves[self.evaluate(grandparent.board)] = grandparent.move
                    node.values.append(self.evaluate(grandparent.board))
        if self.minmax == "max":
            node.value = max(node.values)
        if self.minmax == "min":
            node.value = min(node.values)
        self.evaluation = node.value

    def alphabeta(self, node):
        first = True
        move = ""
        print ("supp")
        for grandparent in node.children:
            next = True
            for parent in grandparent.children:
                for child in parent.children:
                    child.value = self.newevaluate(child.board)
                    parent.values.append(child.value)
                try:
                    if self.minmax == "max":
                        parent.value = max(parent.values)
                    if self.minmax == "min":
                        parent.value = min(parent.values)
                except ValueError:
                    parent.value = self.newevaluate(parent.board)
                grandparent.values.append(parent.value)
                if not first:
                    if self.minmax == "max":
                        if next:
                            grandparent.value = parent.value
                            self.moves[grandparent.value] = grandparent.move
                            next = False
                        else:
                            if grandparent.value <= node.value:
                                break
                            if parent.value < grandparent.value:
                                grandparent.value = parent.value
                                self.moves[grandparent.value] = grandparent.move

                    if self.minmax == "min":
                        if next:
                            grandparent.value = parent.value
                            self.moves[grandparent.value] = grandparent.move
                            next = False
                        else:
                            if grandparent.value >= node.value:
                                break
                            if parent.value > grandparent.value:
                                grandparent.value = parent.value
                                self.moves[grandparent.value] = grandparent.move
            if first:
                if self.minmax == "min":
                    self.moves[max(grandparent.values)] = grandparent.move
                    move = grandparent.move
                    node.values = (max(grandparent.values))
                if self.minmax == "max":
                    self.moves[min(grandparent.values)] = grandparent.move
                    move = grandparent.move
                    node.value = (min(grandparent.values))
                first = False
            else:
                node.value = grandparent.value

        self.evaluation = node.value
        self.moves[node.value] = move

    def find_possible_moves(self, board,Board, colour):
        self.possible_moves = []
        for i in range(Board.LENGTH):
            for j in range(Board.WIDTH):
                if board[i][j]['token'] == " ":
                    if i == 0 and j == 0:
                        if board[i][j]['cell_colour'] == "w":
                            if board[i+1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i+1]+str(j+1)+" "+self.MAP[i]+str(j+1))
                            if board[i][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i]+str(j+1+1)+" "+self.MAP[i]+str(j+1))
                        elif board[i][j]['cell_colour'] == "b":
                            if board[i+1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i+1]+str(j+1)+" "+self.MAP[i]+str(j+1))
                            if board[i][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i]+str(j+1+1)+" "+self.MAP[i]+str(j+1))
                            if board[i+1][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i+1]+str(j+1+1)+" "+self.MAP[i]+str(j+1))
                    elif i == 4 and j == 8:
                        if board[i][j]['cell_colour'] == "w":
                            if board[i-1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i ] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                        elif board[i][j]['cell_colour'] == "b":
                            if board[i-1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i-1][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                    elif i == 0 and j == 8:
                        if board[i][j]['cell_colour'] == "w":
                            if board[i+1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                        elif board[i][j]['cell_colour'] == "b":
                            if board[i+1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i+1][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                    elif i == 4 and j == 0:
                        if board[i][j]['cell_colour'] == "w":
                            if board[i-1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                        elif board[i][j]['cell_colour'] == "b":
                            if board[i-1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i-1][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                    elif i == 0:
                        if board[i][j]['cell_colour'] == "w":
                            if board[i+1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                        elif board[i][j]['cell_colour'] == "b":
                            if board[i+1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i+1][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i+1][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                    elif j == 0:
                        if board[i][j]['cell_colour'] == "w":
                            if board[i][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i+1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board[i-1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                        elif board[i][j]['cell_colour'] == "b":
                            if board[i][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i+1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board[i-1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board[i+1][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i-1][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                    elif i == 4:
                        if board[i][j]['cell_colour'] == "w":
                            if board[i-1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                        elif board[i][j]['cell_colour'] == "b":
                            if board[i-1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i-1][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i-1][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                    elif j == 8:
                        if board[i][j]['cell_colour'] == "w":
                            if board[i][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i+1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board[i-1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                        elif board[i][j]['cell_colour'] == "b":
                            if board[i][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i+1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board[i-1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board[i+1][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i-1][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j - 1+1) + " " + self.MAP[i] + str(j + 1))
                    else:
                        if board[i][j]['cell_colour'] == "w":
                            if board[i+1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board[i-1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                        elif board[i][j]['cell_colour'] == "b":
                            if board[i+1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board[i-1][j]['token'] == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i+1][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i+1][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i-1][j+1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                            if board[i-1][j-1]['token'] == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
        return self.possible_moves