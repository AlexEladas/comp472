class Player:
    def __init__(self, colour, opponent):
        self.colour = colour
        self.attack_type = ""
        self.operationx = ""
        self.operationy = ""
        self.opponent = opponent
        self.number_of_tokens = 22
        self.non_attacking_moves = 0