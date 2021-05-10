# Program: 8 Queen Problem Solutions
# Author: Dody Eid
# Date: May 10, 2021
# Purpose: Python Training


# IMPORTS
import numpy

# SETUP
# Store right diagonals in dictionary
right_diags = {
  "0" : [[1,8]],
  "1" : [[1,7],[2,8]],
  "2" : [[1,6],[2,7],[3,8]],
  "3" : [[1,5],[2,6],[3,7],[4,8]],
  "4" : [[1,4],[2,5],[3,6],[4,7],[5,8]],
  "5" : [[1,3],[2,4],[3,5],[4,6],[5,7],[6,8]],
  "6" : [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8]],
  "7" : [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8]],
  "8" : [[2,1],[3,2],[4,3],[5,4],[6,5],[7,6],[8,7]],
  "9" : [[3,1],[4,2],[5,3],[6,4],[7,5],[8,6]],
  "10" : [[4,1],[5,2],[6,3],[7,4],[8,5]],
  "11" : [[5,1],[6,2],[7,3],[8,4]],
  "12" : [[6,1],[7,2],[8,3]],
  "13" : [[7,1],[8,2]],
  "14" : [[8,1]]
  }

# store left diagonals in a dictionary
left_diags = {
  "0" : [[1,1]],
  "1" : [[1,2],[2,1]],
  "2" : [[1,3],[2,2],[3,1]],
  "3" : [[1,4],[2,3],[3,2],[4,1]],
  "4" : [[1,5],[2,4],[3,3],[4,2],[5,1]],
  "5" : [[1,6],[2,5],[3,4],[4,3],[5,2],[6,1]],
  "6" : [[1,7],[2,6],[3,5],[4,4],[5,3],[6,2],[7,1]],
  "7" : [[1,8],[2,7],[3,6],[4,5],[5,4],[6,3],[7,2],[8,1]],
  "8" : [[2,8],[3,7],[4,6],[5,5],[6,4],[7,3],[8,2]],
  "9" : [[3,8],[4,7],[5,6],[6,5],[7,4],[8,3]],
  "10" : [[4,8],[5,7],[6,6],[7,5],[8,4]],
  "11" : [[5,8],[6,7],[7,6],[8,5]],
  "12" : [[6,8],[7,7],[8,6]],
  "13" : [[7,8],[8,7]],
  "14" : [[8,8]]
}

# Function takes a chess position and returns which right diagonal it covers  
def right_diag(position):
  key_list = list(right_diags.keys())
  val_list=list(right_diags.values())
  #grab index of specific chess position in dict
  place = next(((i, colour.index(position))
        for i, colour in enumerate(val_list)
        if position in colour),
       None)[0]
  return key_list[place]+"right"

#same thing for left diagonals
def left_diag(position):
  key_list = list(left_diags.keys())
  val_list=list(left_diags.values())
  #grab index of specific chess position in dict
  place = next(((i, colour.index(position))
        for i, colour in enumerate(val_list)
        if position in colour),
       None)[0]
  return key_list[place]+"left"

# function spits out list of row, column, left diag, and right diag for a user-given chess position (column,row)
def sc(column,row):
  return list([str(column)+"col",str(row)+"row",right_diag([column,row]),left_diag([column,row])])

# Function takes a list and returns "True" if has repeated elements, false if not
def checkIfDuplicates(listOfElems):
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True
    
# function prints a solution
def show_solutions(*args):
    for i in range(1,len(args)+1):
        print((i,args[i-1]))

# initate variable to keep track of number of solutions
sols = 0

#RUN THE BIG LOOP
# Loop checks all possibilities but quickly skips options that obviously won't work
for a in range(1,9):
    for b in range(1,9):
        if checkIfDuplicates(sc(1,a)+sc(2,b)):
            continue
        for c in range(1,9):
            if checkIfDuplicates(sc(1,a)+sc(2,b)+sc(3,c)):
                continue
            for d in range(1,9):
                if checkIfDuplicates(sc(1,a)+sc(2,b)+sc(3,c)+sc(4,d)):
                    continue
                for e in range(1,9):
                    if checkIfDuplicates(sc(1,a)+sc(2,b)+sc(3,c)+sc(4,d)+sc(5,e)):
                        continue
                    for f in range(1,9):
                        if checkIfDuplicates(sc(1,a)+sc(2,b)+sc(3,c)+sc(4,d)+sc(5,e)+sc(6,f)):
                            continue
                        for g in range(1,9):
                            if checkIfDuplicates(sc(1,a)+sc(2,b)+sc(3,c)+sc(4,d)+sc(5,e)+sc(6,f)+sc(7,g)):
                                continue
                            for h in range(1,9):
                                if checkIfDuplicates(sc(1,a)+sc(2,b)+sc(3,c)+sc(4,d)+sc(5,e)+sc(6,f)+sc(7,g)+sc(8,h)):
                                    continue
                                else:
                                    sols += 1
                                    print('Solution Number ' + str(sols))
                                    show_solutions(a,b,c,d,e,f,g,h)
                                    print(" ")
