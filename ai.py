from board import Board

class AI:
    MAP = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E"
    }
    def __init__(self, colour, opponent):
        self.colour = colour
        self.attack_type = ""
        self.operationx = ""
        self.operationy = ""
        self.opponent = opponent
        self.number_of_tokens = 22
        self.non_attacking_moves = 0
        self.possible_moves = []

    def find_possible_moves(self, board):
        for i in range(board.LENGTH):
            for j in range(board.WIDTH):
                if board.board[i][j].token == " ":
                    if i == 0 and j == 0:
                        if board.board[j][j].cell_colour == "w":
                            if board.board[i+1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i+1]+str(j+1)+" "+self.MAP[i]+str(j+1))
                            if board.board[i][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i]+str(j+1+1)+" "+self.MAP[i]+str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i+1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i+1]+str(j+1)+" "+self.MAP[i]+str(j+1))
                            if board.board[i][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i]+str(j+1+1)+" "+self.MAP[i]+str(j+1))
                            if board.board[i+1][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i+1]+str(j+1+1)+" "+self.MAP[i]+str(j+1))
                    elif i == 4 and j == 8:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i-1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i ] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i-1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                    elif i == 0 and j == 8:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i+1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i+1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                    elif i == 4 and j == 0:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i-1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i-1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                    elif i == 0:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i+1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i+1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                    elif j == 0:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                    elif i == 4:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i-1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i-1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                    elif j == 8:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j-2+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j - 1+1) + " " + self.MAP[i] + str(j))
                    else:
                        if board.board[i][j].cell_colour == "w":
                            if board.board[i+1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                        elif board.board[i][j].cell_colour == "b":
                            if board.board[i+1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i+1] + str(j + 1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j].token == self.colour:
                                self.possible_moves.append(self.MAP[i-1] + str(j+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j+1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i] + str(j-1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i+1][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i + 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j+1].token == self.colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j + 1+1) + " " + self.MAP[i] + str(j+1))
                            if board.board[i-1][j-1].token == self.colour:
                                self.possible_moves.append(self.MAP[i - 1] + str(j - 1+1) + " " + self.MAP[i] + str(j+1))
