import numpy as np
from colorama import Fore, Back, Style

boardsize = 13

class board:
    board = None
    size = None
    state = 0

    def __init__(self, size):
        self.size = size
        self.board = np.zeros(size * size, dtype=int)

    def __str__(self):
        out = ""
        for i in range(self.size+1):
            out += "--"
        out += "\n"
        for i in range(self.size):
            for ii in range(i):
                out += " "
            out += "\\ "
            for j in range(self.size):
                index = i * self.size + j
                value = str(self.board[index])
                if value == "1":
                    out += Back.BLUE + value + Style.RESET_ALL
                elif value == "2":
                    out += Back.RED + value + Style.RESET_ALL
                else:
                    out += value
                out += " "
            out += "\\\n"
        for i in range(self.size):
            out += " "
        for i in range(self.size+1):
            out += "--"
        return out

    def put(self, pos):
        self.state += 1
        i = int(ord(pos[0]) - 97) # ord('a') == 97
        j = int(pos[1:3]) - 1
        index = i * self.size + j
        value = 1 if (self.state % 2 != 0) else 2
        self.board.put(index, value)

    def getLastPlayer(self):
        value = 1 if (self.state % 2 != 0) else 2
        return value

if __name__ == "__main__":
    infile = open('raw_games_small.dat', 'r')
    print("Playing games", end='')
    for line in infile:
        print(".", end='')
        game = board(boardsize)
        moves = line.split()
        for move in moves:
            game.put(move)
    print()
    print("End")