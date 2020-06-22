from board import board

"""
The program read games and write game outcome to the output file. 
The output file name is generated based on input file name.
The input raw_games.dat contains a list of moves corresponding to a 13x13 hex game on each line. 
A game represented by space separated coordinates. 
"""

boardsize = 13

def generatescoring(filename):
    print("Reading input file:", filename)
    infile = open(filename, "r")

    print("Creating output file.")
    filenames = filename.split(".")
    outfilename = filenames[0] + "_scored." + filenames[1]
    outfile = open(outfilename, "w")

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
