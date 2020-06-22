import numpy as np
from colorama import Fore, Back, Style
"""
Bord class for hex table
"""

class board:
    board = None #np.ndarray
    size = None #board's size
    state = 0 #increased by 1 if 1st or 2nd player moves

    def __init__(self, size):
        self.size = size
        self.board = np.zeros(size * size, dtype=int)

    # returns csv as text
    def csv(self):
        out = ""
        for it in self.board:
            out += str(it) + ","
        return out

    # returns the current game as text, pretty print for conolse.
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

    # puts a marker to a position with the current player
    def put(self, pos):
        self.state += 1
        value = 1 if (self.state % 2 != 0) else 2
        self.put(self, pos, value)

    # puts a marker to a position with parameterized value
    def put(self, pos, value):
        i = int(ord(pos[0]) - 97) # ord('a') == 97
        j = int(pos[1:3]) - 1
        index = i * self.size + j
        self.board.put(index, value)

    # returns with the last moved player
    def getLastPlayer(self):
        return \
            1 if (self.state % 2 != 0) else 2

    # returns true is the first player won
    def firstPlayerWins(self, a = True, b = False):
        return\
            a if (self.state % 2 != 0) else b