# Program: eightqueenproblem.py
# Author: Dody Eid
# Date: May 10, 2021
# Purpose: Solve the 8 Queen Problem in Chess


# IMPORTS
import numpy

# SETUP
# function that gets forward slash or backward slash diagonal (the slant) of a piece (in column a and row b) on an nxn board!
def diag(a,b,n,slant):
    if slant == "right":
        if a < b:
            return slant + str(a + (n-b)) + "z1"
        if a > b:
            return slant + str(b + (n-a)) + "z2"
        if a == b:
            return slant + str(n)
    if slant == "left":
        if b > n-(a-1):
            return slant + str((n-a) + (n-b)) + "z1"
        if b < n-(a-1):
            return slant + str(b+a) + "z2"
        if a + b == 9:
            return slant + str(n)
    

# function spits out list of row, column, left diag, and right diag for a user-given chess position (two-element list with column, row)
def sc(var):
  return list([str(var[0])+"col",str(var[1])+"row",diag(var[0],var[1],8,"right"),diag(var[0],var[1],8,"left")])

# Function takes a list and returns "True" if has repeated elements, false if not ... this is to check if pieces attack later.
def checkIfDuplicates(listOfElems):
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True
    
# function prints a piece-combination solution... to print solutions later
def show_solutions(*args):
    for i in range(1,len(args)+1):
        print((i,args[i-1]))
        
# initate variable to keep track of number of solutions
sols = 0

#RUN THE BIG LOOP
# Loop places one queen at a time in each column, checks if queens attack, then adjusts accordingly.
for a in range(1,9):
    for b in range(1,9):
        if checkIfDuplicates(sc((1,a))+sc((2,b))):
            continue
        for c in range(1,9):
            if checkIfDuplicates(sc((1,a))+sc((2,b))+sc((3,c))):
                continue
            for d in range(1,9):
                if checkIfDuplicates(sc((1,a))+sc((2,b))+sc((3,c))+sc((4,d))):
                    continue
                for e in range(1,9):
                    if checkIfDuplicates(sc((1,a))+sc((2,b))+sc((3,c))+sc((4,d))+sc((5,e))):
                        continue
                    for f in range(1,9):
                        if checkIfDuplicates(sc((1,a))+sc((2,b))+sc((3,c))+sc((4,d))+sc((5,e))+sc((6,f))):
                            continue
                        for g in range(1,9):
                            if checkIfDuplicates(sc((1,a))+sc((2,b))+sc((3,c))+sc((4,d))+sc((5,e))+sc((6,f))+sc((7,g))):
                                continue
                            for h in range(1,9):
                                if checkIfDuplicates(sc((1,a))+sc((2,b))+sc((3,c))+sc((4,d))+sc((5,e))+sc((6,f))+sc((7,g))+sc((8,h))):
                                    continue
                                else:
                                    sols += 1
                                    print('Solution Number ' + str(sols))
                                    show_solutions(a,b,c,d,e,f,g,h)
                                    print(" ")
