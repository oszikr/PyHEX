# PyHEX
All rights reserved.
Open first: https://github.com/oszikr/QtHEX

raw_games.dat:
Contains 10985 games and 550983 states.

raw_games_small.dat:
Contains first 10 games from raw_games.dat.

preprocessing1.py:
Create raw_games_scored.dat from raw_games.dat.
Create raw_games_small_scored.dat from raw_games_small.dat.
The *_scored.dat files contains labels to each line. The label is the game outcome game.

preprocessing2.py:
Create raw_games_scored_states.csv from raw_games_scored.dat.
Create raw_games_small_scored_states.csv from raw_games_small_scored.dat.
The *_scored_states.csv files contains each game states and labels. The label is the game outcome for all game states.

learn.py:
Creating model.h5 and model.json NNET files and testing it. test size is 20%.

test.py:
Load NNET and test it. The test is same as learn.py

predict.py:
It loads the NNET, get input and print prediction.

service.py:
Service process for CPP application. It loads NNet and ask input. The input is an array of states. The output is an
array of predictions.

util.py:
Functions for save and load NNET, labelencoders, onehotencoder and other.

board.py:
Class for HEX board.

requirements.txt:
installed python packages (pip freeze, windows 10, python3.6).
Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47)
[MSC v.1916 64 bit (AMD64)] on win32

requirements_b.txt:
installed python packages (pip freeze, debian linux, vm, python3.5).
Python 3.5.3 (default, Jul  9 2020, 13:00:10)
[GCC 6.3.0 20170516] on linux
