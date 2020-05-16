What is it?
---------- 

Mastermind is a very popular sequence-guessing game, whrein the player has to guess the sequnce
of colors that another player has set. Here we are using numbers intead of colors.


How it works
------------
Once the program is run, it will give a choice of number of players(1 for single layer and 2 for double). In single player mode,
number to be guessed is set automatically by the program using the 'random' module. For two player mode, one of player has
to input the number to be guessed. 

When the number to be guessed is ready (say 1234), the program will prompt for a guess from the user (or player2).
Suppose the user guess is 1432, say, it will then give an output some thing like this:

Guess no. 1: 1432 : positions:2	numbers:2

What it means-
- Positions indicates the number of digits that you got correct and are in the correct position as the number to be guessed.
- Numbers indicates the number of digits that are correct but are in the wrong positions.

Using this information, the user has to correctly guess the number pattern, within 10 guesses.



