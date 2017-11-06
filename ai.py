from board import Board
from node import Node
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
        self.future_board = []
        self.moves = {}

    def evaluate(self, board):
        score = 0
        for i in range(board.LENGTH):
            for j in range(board.WIDTH):
                if board.board[i][j].token == "G":
                    score += 100 * (i+1) + 50 * (j + 1)
                if board.board[i][j].token == "R":
                    score -= 100 * (i+1) + 50 * (j + 1)
        return score

    def build_tree(self, board, ai, opponent):
        tmpai = ai.number_of_tokens
        tmpop = opponent.number_of_tokens
        future_board = Board()
        root = Node(future_board,0,"")
        future_board.board = board.board
        #print(self.find_possible_moves(future_board, ai.colour))
        depth = 1
        for move in self.find_possible_moves(future_board, ai.colour):
            future_board = Board()
            if depth == 1:
                future_board.move(move, ai)
                if future_board.check_if_attacking_move(move, ai):
                    future_board.attack(move, ai)
                #future_board.display()
                root.add_child(Node(future_board, depth, move))
                #self.find_possible_moves(future_board,ai.opponent)
                #print (self.find_possible_moves(future_board, ai.opponent))
        depth = 2
        x = 1
        #print (len(root.children))
        for child in root.children:

            #print(self.find_possible_moves(future_board, ai.opponent))
            for move in self.find_possible_moves(child.board, ai.opponent):
                future_board = copy.deepcopy(child.board)
                #future_board.display()
                #print(self.find_possible_moves(future_board, ai.opponent))
                future_board.move(move, opponent)
                if future_board.check_if_attacking_move(move, opponent):
                    future_board.attack(move, opponent)
                #future_board.display()
                #print(move)
                child.add_child(Node(future_board, depth, move))
            #print(self.find_possible_moves(future_board,ai.opponent))
        #print(depth)
        depth = 3
        for parent in root.children:
            for child in parent.children:
                for move in self.find_possible_moves(child.board, ai.colour):
                    future_board = copy.deepcopy(child.board)
                #future_board.display()
                    future_board.move(move, ai)
                    #future_board.display()

                    if future_board.check_if_attacking_move(move, ai):
                        future_board.attack(move, ai)
                        #future_board.display()
                    #future_board.display()
                    #print(move)
                    child.add_child(Node(future_board, depth, move))
                    #self.find_possible_moves(future_board, ai.colour)
                    # print (self.find_possible_moves(future_board, ai.opponent))
        ai.number_of_tokens = tmpai
        opponent.number_of_tokens = tmpop
        self.minimax(root, opponent)
    def minimax(self, node, opponent):
        #node.board.display()
        for grandparent in node.children:
            for parent in grandparent.children:
                for child in parent.children:
                    child.value = self.evaluate(child.board)
                    #print(child.value)
                    parent.values.append(child.value)
                #print(parent.values)
                try:
                    if self.minmax == "max":
                        parent.value = max(parent.values)
                    if self.minmax == "min":
                        parent.value = min(parent.values)
                except ValueError:
                    parent.value = self.evaluate(parent.board)
                #print(parent.max)
                #print(parent.min)
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
        #print(node.value)
        #print(self.moves[node.value])


    def find_possible_moves(self, board, colour):
        self.possible_moves = []
        for i in range(board.LENGTH):
            for j in range(board.WIDTH):
                if board.board[i][j].token == " ":
                    if i == 0 and j == 0:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i+1][j].token == colour:
                                self.possible_moves.append(self.MAP[i+1]+str(j+1)+" "+self.MAP[i]+str(j+1))
                            if board.board[i][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i]+str(j+1+1)+" "+self.MAP[i]+str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i+1][j].token == colour:
                                self.possible_moves.append(self.MAP[i+1]+str(j+1)+" "+self.MAP[i]+str(j+1))
                            if board.board[i][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i]+str(j+1+1)+" "+self.MAP[i]+str(j+1))
                            if board.board[i+1][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i+1]+str(j+1+1)+" "+self.MAP[i]+str(j+1))
                    elif i == 4 and j == 8:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i-1][j].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i ] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i-1][j].token == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                    elif i == 0 and j == 8:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i+1][j].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i+1][j].token == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                    elif i == 4 and j == 0:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i-1][j].token == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i-1][j].token == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                    elif i == 0:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i+1][j].token == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i+1][j].token == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                    elif j == 0:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j].token == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j].token == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j].token == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j].token == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                    elif i == 4:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i-1][j].token == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i-1][j].token == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                    elif j == 8:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j].token == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j].token == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-2+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j].token == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j].token == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j - 1+1) + " " + self.MAP[i] + str(j + 1))
                    else:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i+1][j].token == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j].token == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i+1][j].token == colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j].token == colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j+1].token == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j-1].token == colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
        return self.possible_moves