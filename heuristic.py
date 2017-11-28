MAP = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4
      }
MAP2 = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E"
}



def check_if_attacking_move(board, move, player):
    x, y = move.split(" ", 1)
    currenty = MAP[x[0].upper()]
    currentx = int(x[1]) - 1
    nexty = MAP[y[0].upper()]
    nextx = int(y[1]) - 1
    
    if currentx != nextx and currenty != nexty:
        if nextx > currentx and nexty > currenty:
            if nexty != 4 and nextx != 8:  # border check
                if board[nexty + 1][nextx + 1]['token'] == player:
                    return True
            if currenty != 0 and currentx != 0:
                if board[currenty - 1][currentx - 1]['token'] == player:
                    return True
        if nextx > currentx and nexty < currenty:
            if nexty != 0 and nextx != 8:
                if board[nexty - 1][nextx + 1]['token'] == player:
                    return True
            if currenty != 4 and currentx != 0:
                if board[currenty + 1][currentx - 1]['token'] == player:
                    return True
        if nextx < currentx and nexty < currenty:
            if nexty != 0 and nextx != 0:
                if board[nexty - 1][nextx - 1]['token'] == player:
                    return True
            if currenty != 4 and currentx != 8:
                if board[currenty + 1][currentx + 1]['token'] == player:
                    return True
        if nextx < currentx and nexty > currenty:
            if nexty != 4 and nextx != 0:
                if board[nexty + 1][nextx - 1]['token'] == player:
                    return True
            if currenty != 0 and currentx != 8:
                if board[currenty - 1][currentx + 1]['token'] == player:
                    return True
    if currenty == nexty:
        if nextx > currentx:
            if nextx != 8:
                if board[nexty][nextx + 1]['token'] == player:
                    
                    return True
            if currentx != 0:
                if board[nexty][currentx - 1]['token'] == player:
                    
                    return True
        elif nextx < currentx:
            if nextx != 0:
                if board[currenty][nextx - 1]['token'] == player:
                    
                    return True
            if currentx != 8:
                if board[currenty][currentx + 1]['token'] == player:
                    
                    return True
    elif currentx == nextx:
        if nexty > currenty:
            if nexty != 4:
                if board[nexty + 1][nextx]['token'] == player:
                    
                    return True
            if currenty != 0:
                if board[currenty - 1][currentx]['token'] == player:
                    
                    return True
        if nexty < currenty:
            if nexty != 0:
                if board[nexty - 1][currentx]['token'] == player:
                    
                    return True
            if currenty != 4:
                if board[currenty + 1][currentx]['token'] == player:
                    return True
    return False

def find_moves(board, i, j):
    possible_moves = []
    if i == 0 and j == 0:
        if board[i][j]['cell_colour'] == "w":
            if board[i + 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1))
            if board[i][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1))
        elif board[i][j]['cell_colour'] == "b":
            if board[i + 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1))
            if board[i][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1))
            if board[i + 1][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j + 1 + 1))
    elif i == 4 and j == 8:
        if board[i][j]['cell_colour'] == "w":
            if board[i - 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1))
            if board[i][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j - 1 + 1))
        elif board[i][j]['cell_colour'] == "b":
            if board[i - 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1))
            if board[i][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j - 1 + 1))
            if board[i - 1][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j - 1 + 1))
    elif i == 0 and j == 8:
        if board[i][j]['cell_colour'] == "w":
            if board[i + 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j + 1))
            if board[i][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j - 1 + 1))
        elif board[i][j]['cell_colour'] == "b":
            if board[i + 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j + 1))
            if board[i][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j - 1 + 1))
            if board[i + 1][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j - 1 + 1))
    elif i == 4 and j == 0:
        if board[i][j]['cell_colour'] == "w":
            if board[i - 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1))
            if board[i][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1 + 1))
        elif board[i][j]['cell_colour'] == "b":
            if board[i - 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1))
            if board[i][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1 + 1))
            if board[i - 1][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1 + 1))
    elif i == 0:
        if board[i][j]['cell_colour'] == "w":
            if board[i + 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j + 1))
            if board[i][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j - 1 + 1))
            if board[i][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1 + 1))
        elif board[i][j]['cell_colour'] == "b":
            if board[i + 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j + 1))
            if board[i][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j - 1 + 1))
            if board[i][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1 + 1))
            if board[i + 1][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j + 1 + 1))
            if board[i + 1][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j - 1 + 1))
    elif j == 0:
        if board[i][j]['cell_colour'] == "w":
            if board[i][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1 + 1))
            if board[i + 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j + 1))
            if board[i - 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1))
        elif board[i][j]['cell_colour'] == "b":
            if board[i][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1 + 1))
            if board[i + 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j + 1))
            if board[i - 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1))
            if board[i + 1][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j + 1 + 1))
            if board[i - 1][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1 + 1))
    elif i == 4:
        if board[i][j]['cell_colour'] == "w":
            if board[i - 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1))
            if board[i][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1 + 1))
            if board[i][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j - 1 + 1))
        elif board[i][j]['cell_colour'] == "b":
            if board[i - 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1))
            if board[i][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1 + 1))
            if board[i][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j - 1 + 1))
            if board[i - 1][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1 + 1))
            if board[i - 1][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j - 1 + 1))
    elif j == 8:
        if board[i][j]['cell_colour'] == "w":
            if board[i][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j - 1 + 1))
            if board[i + 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j + 1))
            if board[i - 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1))
        elif board[i][j]['cell_colour'] == "b":
            if board[i][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j - 1 + 1))
            if board[i + 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j + 1))
            if board[i - 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1))
            if board[i + 1][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j - 1 + 1))
            if board[i - 1][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j - 1 + 1))
    else:
        if board[i][j]['cell_colour'] == "w":
            if board[i + 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j + 1))
            if board[i - 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1) )
            if board[i][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1 + 1))
            if board[i][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j - 1 + 1))
        elif board[i][j]['cell_colour'] == "b":
            if board[i + 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j + 1))
            if board[i - 1][j]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1))
            if board[i][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j + 1 + 1))
            if board[i][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i] + str(j - 1 + 1))
            if board[i + 1][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j + 1 + 1))
            if board[i + 1][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i + 1] + str(j - 1 + 1))
            if board[i - 1][j + 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j + 1 + 1))
            if board[i - 1][j - 1]['token'] == " ":
                possible_moves.append(MAP2[i] + str(j + 1) + " " + MAP2[i - 1] + str(j - 1 + 1))
    return possible_moves