# Eight Queen Problem
The python file solves the 8 queen problem in chess, explained here: https://en.wikipedia.org/wiki/Eight_queens_puzzle

## Method
I save the diagonals of the chess board into two dictionaries. I then write a function that takes some chess position as an input and outputs all the "attacked" ranges. I can then check if *n* positions/pieces attack each other. I use a brute-force nested-for-loop algorithm to check all possibilities, but I use continue statements to quickly skip over solutions that do not work. When 8 pieces do not attack each other, I print the result. 92 distinct solutions are found!
