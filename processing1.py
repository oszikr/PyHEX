from board import board
from datetime import datetime

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

    outfilename2 = filenames[0] + "_steps." + filenames[1]
    outfile2 = open(outfilename2, "w")

    print("Playing games:")
    s = 0
    i = 0
    for line in infile:
        i += 1
        print("Game", i)
        game = board(boardsize)
        moves = line.split()
        j = 0;
        for move in moves:
            #print(move)
            #game.put(move)
            print(game.__str__())
            j += 1
            s += 1;
        print(game)
        print(game.firstPlayerWins())
        print()
        outfile.write(str(game.firstPlayerWins("positive", "negative")) + '\n')
        outfile2.write(str(j) + '\n')
    print("Total", s, "states")
    outfile.close()
    outfile2.close()
    print("End.")


if __name__ == "__main__":
    start_time = datetime.now().strftime("%H:%M:%S")
    print("Start Time =", start_time)

    generatescoring("raw_games_small.dat")
    generatescoring("raw_games.dat")

    stop_time = datetime.now().strftime("%H:%M:%S")
    print("Start Time =", start_time)
    print("Stop Time  =", stop_time)
