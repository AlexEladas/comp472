from cell import Cell


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
                        x.token = ""
                else:
                    x.token = "G"
                row.append(x)
            column.append(list(row))
        self.board = column

    def check_if_valid(self, move, player):
        x, y = move.split(" ", 1)
        currenty = self.MAP[x[0]]
        currentx = int(x[1]) - 1
        nexty = self.MAP[y[0]]
        nextx = int(y[1]) - 1
        if self.board[currenty][currentx].token == "" or self.board[nexty][nextx].token != "" or self.board[currenty][currentx].token != player.colour:
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

    def check_if_attacking_move(self, move, player):
        x, y = move.split(" ", 1)
        currenty = self.MAP[x[0]]
        currentx = int(x[1]) - 1
        nexty = self.MAP[y[0]]
        nextx = int(y[1]) - 1

        if self.board[currenty][currentx].cell_colour == "b":
            if currentx != nextx and currenty != nexty:
                if nextx > currentx and nexty > currenty:
                    if currenty != 4 and nextx != 8:
                        if self.board[currenty + 1][nextx + 1].token != player.colour:
                            player.attack_type = "forward"
                            return True
                    if currenty != 0 and currentx != 0:
                        if self.board[currenty - 1][currentx - 1].token != player.colour:
                            player.attack_type = "backward"
                            return True
                if nextx > currentx and nexty < currenty:
                    if nexty != 0 and nextx != 8:
                        if self.board[nexty - 1][nextx + 1].token != player.colour:
                            player.attack_type = "forward"
                            return True
                    if currenty != 0 and nextx != 0:
                        if self.board[currenty - 1][nextx - 1].token != player.colour:
                            player.attack_type = "backward"
                            return True
                if nextx < currentx and nexty < currenty:
                    if nexty != 0 and nextx != 8:
                        if self.board[nexty - 1][nextx + 1].token != player.colour:
                            player.attack_type = "forward"
                            return True
                    if self.board[currenty + 1][currentx + 1].token != player.colour:
                        if currenty != 4 and currentx != 8:
                            player.attack_type = "backward"
                            return True
                if nextx < currentx and nexty > currenty:
                    if nexty != 4 and nextx != 0:
                        if self.board[nexty + 1][nextx - 1].token != player.colour:
                            player.attack_type = "forward"
                            return True
                    if currenty != 0 and nextx != 8:
                        if self.board[currenty - 1][nextx + 1].token != player.colour:
                            player.attack_type = "backward"
                            return True
        else:
            if currenty == nexty:
                if nextx > currentx:
                    if nextx != 8:
                        if self.board[currenty][nextx + 1].token != player.colour:
                            player.attack_type = "forward"
                            return True
                    if currentx != 0:
                        if self.board[currenty][currentx - 1].token != player.colour:
                            player.attack_type = "backward"
                            return True
                elif nextx < currentx:
                    if nextx != 0:
                        if self.board[currenty][nextx - 1].token != player.colour:
                            player.attack_type = "forward"
                            return True
                    if currentx != 8:
                        if self.board[currenty][currentx + 1].token != player.colour:
                            player.attack_type = "backward"
                            return True
            elif currentx == nextx:
                if nexty > currenty:
                    if nexty != 4:
                        if self.board[nexty + 1][currentx].token != player.colour:
                            player.attack_type = "forward"
                            return True
                    if currenty != 0:
                        if self.board[currenty - 1][currentx].token != player.colour:
                            player.attack_type = "backward"
                            return True
                if nexty < currenty:
                    if nexty != 0:
                        if self.board[nexty - 1][currentx].token != player.colour:
                            player.attack_type = "forward"
                            return True
                    if currenty != 4:
                        if self.board[currenty + 1][currentx].token != player.colour:
                            player.attack_type = "backward"
                            return True
        player.attack_type = "defensive"
        return False

    def attack(self):
        pass