from cell import Cell
import operator
from pprint import pprint


class Board:

    WIDTH = 9
    LENGTH = 5
    MAP = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4
          }

    def __init__(self):
        column = []
        for i in range(self.LENGTH):
            row = []
            for j in range(self.WIDTH):
                x = Cell()
                if i % 2 == j % 2:
                    x.cell_colour = "b"
                else:
                    x.cell_colour = "w"
                if i == 0 or i == 1:
                    x.token = "R"
                elif i == 2:
                    if j > 4:
                        x.token = "R"
                    elif j < 4:
                        x.token = "G"
                    else:
                        x.token = " "
                else:
                    x.token = "G"
                row.append(x)
            column.append(list(row))
        self.board = column

    def check_if_valid(self, move, player):
        try:
            x, y = move.split(" ", 1)
            currenty = self.MAP[x[0]]
            currentx = int(x[1]) - 1
            nexty = self.MAP[y[0]]
            nextx = int(y[1]) - 1
            if self.board[currenty][currentx].token == " " or self.board[nexty][nextx].token != " " or self.board[currenty][currentx].token != player.colour:
                return False
            if self.board[currenty][currentx].cell_colour == "w":
                if currenty == nexty:
                    if nextx == (currentx + 1) or nextx == (currentx - 1):
                        return True
                    else:
                        return False
                else:
                    if nextx == currentx:
                        return True
                    else:
                        return False
            if self.board[currenty][currentx].cell_colour == "b":
                if currenty == nexty:
                    if nextx == (currentx + 1) or nextx == (currentx - 1):
                        return True
                    else:
                        return False
                else:
                    if nextx == currentx or nextx == (currentx + 1) or nextx == (currentx - 1):
                        return True
                    else:
                        return False
        except ValueError:
            return False

    def move(self, move, player):
        x, y = move.split(" ", 1)
        currenty = self.MAP[x[0]]
        currentx = int(x[1]) - 1
        nexty = self.MAP[y[0]]
        nextx = int(y[1]) - 1
        self.board[currenty][currentx].token = " "
        self.board[nexty][nextx].token = player.colour

    def check_if_attacking_move(self, move, player):
        x, y = move.split(" ", 1)
        currenty = self.MAP[x[0]]
        currentx = int(x[1]) - 1
        nexty = self.MAP[y[0]]
        nextx = int(y[1]) - 1

        if currentx != nextx and currenty != nexty:
            if nextx > currentx and nexty > currenty:
                if currenty != 4 and nextx != 8:
                    if self.board[nexty + 1][nextx + 1].token == player.opponent:
                        player.attack_type = "forward"
                        return True
                if currenty != 0 and currentx != 0:
                    if self.board[currenty - 1][currentx - 1].token == player.opponent:
                        player.attack_type = "backward"
                        return True
            if nextx > currentx and nexty < currenty:
                if nexty != 0 and nextx != 8:
                    if self.board[nexty - 1][nextx + 1].token == player.opponent:
                        player.attack_type = "forward"
                        return True
                if currenty != 0 and nextx != 0:
                    if self.board[currenty + 1][currentx - 1].token == player.opponent:
                        player.attack_type = "backward"
                        return True
            if nextx < currentx and nexty < currenty:
                if nexty != 0 and nextx != 8:
                    if self.board[nexty - 1][nextx - 1].token == player.opponent:
                        player.attack_type = "forward"
                        return True
                if self.board[currenty + 1][currentx + 1].token == player.opponent:
                    if currenty != 4 and currentx != 8:
                        player.attack_type = "backward"
                        return True
            if nextx < currentx and nexty > currenty:
                if nexty != 4 and nextx != 0:
                    if self.board[nexty + 1][nextx - 1].token == player.opponent:
                        player.attack_type = "forward"
                        return True
                if currenty != 0 and nextx != 8:
                    if self.board[currenty - 1][currentx + 1].token == player.opponent:
                        player.attack_type = "backward"
                        return True
        if currenty == nexty:
            if nextx > currentx:
                if nextx != 8:
                    if self.board[nexty][nextx + 1].token == player.opponent:
                        player.attack_type = "forward"
                        return True
                if currentx != 0:
                    if self.board[nexty][currentx - 1].token == player.opponent:
                        player.attack_type = "backward"
                        return True
            elif nextx < currentx:
                if nextx != 0:
                    if self.board[currenty][nextx - 1].token == player.opponent:
                        player.attack_type = "forward"
                        return True
                if currentx != 8:
                    if self.board[currenty][currentx + 1].token == player.opponent:
                        player.attack_type = "backward"
                        return True
        elif currentx == nextx:
            if nexty > currenty:
                if nexty != 4:
                    if self.board[nexty + 1][nextx].token == player.opponent:
                        player.attack_type = "forward"
                        return True
                if currenty != 0:
                    if self.board[currenty - 1][currentx].token == player.opponent:
                        player.attack_type = "backward"
                        return True
            if nexty < currenty:
                if nexty != 0:
                    if self.board[nexty - 1][currentx].token == player.opponent:
                        player.attack_type = "forward"
                        return True
                if currenty != 4:
                    if self.board[currenty + 1][currentx].token == player.opponent:
                        player.attack_type = "backward"
                        return True
        player.attack_type = "defensive"
        player.non_attacking_moves += 1
        return False

    def attack(self, move, player):
        self.non_attacking_moves = 0
        x, y = move.split(" ", 1)
        currenty = self.MAP[x[0]]
        currentx = int(x[1]) - 1
        nexty = self.MAP[y[0]]
        nextx = int(y[1]) - 1
        i = 1
        if player.attack_type == "forward":

            if nextx > currentx and nexty > currenty:
                while (nexty + i) < 5 and (nextx + i) < 9:
                    if self.board[nexty + i][nextx + i].token == player.opponent:
                        self.board[nexty + i][nextx + i].token = " "
                    else:
                        player.number_of_tokens -= i - 1
                        break
                    i += 1
            elif nextx > currentx and nexty < currenty:
                while (nexty - i) >= 0 or (nextx + i) < 9:
                    if self.board[nexty - i][nextx + i].token == player.opponent:
                        self.board[nexty - i][nextx + i].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1
            elif nextx < currentx and nexty < currenty:
                while (nexty - i) >= 0 or (nextx - i) >= 0:
                    if self.board[nexty - i][nextx - i].token == player.opponent:
                        self.board[nexty - i][nextx - i].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1
            elif nextx < currentx and nexty > currenty:
                while (nexty + i) < 5 or (nextx - i) >= 0:
                    if self.board[nexty + i][nextx - i].token == player.opponent:
                        self.board[nexty + i][nextx - i].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1
            elif nextx > currentx:
                while (nextx + i) < 9:
                    if self.board[nexty][nextx + i].token == player.opponent:
                        self.board[nexty][nextx + i].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1
            elif nextx < currentx:
                while (nextx - i) >= 0:
                    if self.board[nexty][nextx - i].token == player.opponent:
                        self.board[nexty][nextx - i].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1
            elif nexty > currenty:
                while (nexty + i) < 5:
                    if self.board[nexty + i][nextx].token == player.opponent:
                        self.board[nexty + i][nextx].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1
            elif nexty < currenty:
                while (currenty + i) >= 0:
                    if self.board[nexty - i][nextx].token == player.opponent:
                        self.board[nexty - i][nextx].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1

        if player.attack_type == "backward":
            if nextx > currentx and nexty > currenty:
                while (nexty - i) >= 0 and (currentx - i) >= 0:
                    if self.board[currenty - i][currentx - i].token == player.opponent:
                        self.board[currenty - i][currentx - i].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1
            elif nextx > currentx and nexty < currenty:
                while (currenty + i) < 5 and (currentx - i) >= 0:
                    if self.board[currenty + i][currentx - i].token == player.opponent:
                        self.board[currenty + i][currentx - i].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1
            elif nextx < currentx and nexty < currenty:
                while (currenty + i) < 5 and (currentx + i) < 9:
                    if self.board[currenty + i][currentx + i].token == player.opponent:
                        self.board[currenty + i][currentx + i].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1
            elif nextx < currentx and nexty > currenty:
                while (currenty - i) >= 0 and (currentx + i) < 9:
                    if self.board[currenty - i][currentx + i].token == player.opponent:
                        self.board[currenty - i][currentx + i].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1
            elif nextx > currentx:
                while (currentx - i) >= 0:
                    if self.board[currenty][currentx - i].token == player.opponent:
                        self.board[currenty][currentx - i].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1
            elif nextx < currentx:
                while (currentx + i) < 9:
                    if self.board[currenty][currentx + i].token == player.opponent:
                        self.board[currenty][currentx + i].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1
            elif nexty > currenty:
                while (currenty - i) >= 0:
                    if self.board[currenty - i][currentx].token == player.opponent:
                        self.board[currenty - i][currentx].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1
            elif nexty < currenty:
                while (currenty + i) < 5:
                    if self.board[currenty + i][currentx].token == player.opponent:
                        self.board[currenty + i][currentx].token = " "
                    else:
                        player.number_of_tokens -= i
                        break
                    i += 1
        else:
            pass

    def display(self):
        pprint ([[cell.token for cell in row] for row in self.board])