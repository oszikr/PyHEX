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

def generatescoredstates(gamesfilename, scoresfilename, stepsfilename):
    gamesfile = open(gamesfilename, "r")
    scoresfile = open(scoresfilename, "r")
    stepsfile = open(stepsfilename, "r")
    filenames = gamesfilename.split(".")
    outfile = open(filenames[0] + "_scored_states.csv", "w")

    scores = np.array([], dtype=bool)
    for line in scoresfile:
        line = line.strip()
        scores = np.append(scores, line)

    steps = np.array([], dtype=int)
    for line in stepsfile:
        line = line.strip()
        steps = np.append(steps, line)

    print("Playing games:")
    i = 0
    for line in gamesfile:
        score = scores[i]
        step = int(steps[i])-1
        print("Game", i, score, step)
        game = board(boardsize)
        moves = line.split()
        j = 0
        for move in moves:
            game.put(move)
            progress = round(j / step, 1)
            scoredstate = game.csv() + "," + score + "," + str(progress)
            outfile.write(scoredstate + "\n")
            j += 1
        i += 1
    outfile.close()
    print("End.")

if __name__ == "__main__":
    generatescoredstates("raw_games_small.dat", "raw_games_small_scored.dat", "raw_games_small_steps.dat")
    #generatescoredstates("raw_games.dat", "raw_games_scored.dat", "raw_games_steps.dat")