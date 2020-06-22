from board import board
import numpy as np
"""
The program read games and outcomes, and write all states with the game outcome to the output file. 
The output file name is generated based on input file name.
The input raw_games.dat contains a list of moves corresponding to a 13x13 hex game on each line. 
A game represented by space separated coordinates. 
The input raw_games_scored.dat contains game outcomes on each line.
"""

boardsize = 13

def generatescoredstates(gamesfilename, scoresfilename):
    gamesfile = open(gamesfilename, "r")
    scoresfile = open(scoresfilename, "r")
    filenames = gamesfilename.split(".")
    outfile = open(filenames[0] + "_scored_states.csv", "w")

    scores = np.array([], dtype=bool)
    for line in scoresfile:
        line = line.strip()
        scores = np.append(scores, line)
    print("Playing games:")
    i = 0
    for line in gamesfile:
        score = scores[i]
        print("Game", i, score)
        game = board(boardsize)
        moves = line.split()
        for move in moves:
            game.put(move)
            scoredstate = game.csv() + score
            outfile.write(scoredstate + "\n");
        i += 1
    outfile.close()
    print("End.")

if __name__ == "__main__":
    generatescoredstates("raw_games_small.dat", "raw_games_small_scored.dat")
    generatescoredstates("raw_games.dat", "raw_games_scored.dat")