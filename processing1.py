from board import board
boardsize = 13

def generatescoring(filename):
    infile = open(filename, "r")
    filenames = filename.split(".")
    outfile = open(filenames[0] + "_scored." + filenames[1], "w")
    print("Playing games:")
    i = 0
    for line in infile:
        i += 1
        print("Game", i)
        game = board(boardsize)
        moves = line.split()
        for move in moves:
            game.put(move)
        print(game)
        print(game.firstPlayerWins())
        print()
        outfile.write(str(game.firstPlayerWins("positive", "negative")) + '\n')
    outfile.close()
    print("End.")

if __name__ == "__main__":
    generatescoring("raw_games_small.dat")
    generatescoring("raw_games.dat")