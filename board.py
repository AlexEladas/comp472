from cell import Cell

class Board:
    WIDTH = 9
    LENGTH = 5
    def __init__(self):
        column = []
        for i in range(5):
            row = []
            for j in range(9):
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