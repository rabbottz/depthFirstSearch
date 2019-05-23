'''
Class: CPSC 427 
Team Member 1: Andrew Abbott
Team Member 2: None
Submitted By Andrew Abbott
GU Username: aabbott
File Name: proj5.py
Generates first-level child states from an initial state of the 8-puzzle
Reference: An Eight-Puzzle Solver in Python, https://gist.github.com/flatline/8382021
Usage: python proj5.py
'''

from copy import deepcopy
from collections import deque


class EightPuzzle:
    def __init__(self,parent):
        #state_lst now holds the root, the parent state
        self.state_lst = [[row for row in parent]]

    #displays all states in state_lst
    def display(self):
        i = 0
        for state in self.state_lst:
            print('Node: ' + str(i + 1))
            i = i + 1
            for row in state:
                print row
            print ""
        
    #returns (row,col) of value in state indexed by state_idx  
    def find_coord(self, value, state_idx):
    
        for row in range(3):
            for col in range(3):
                if self.state_lst[state_idx][row][col] == value:
                    return (row,col)
        
                
    #returns list of (row, col) tuples which can be swapped for blank
    #these form the legal moves of the state indexed by state_idx
    def get_new_moves(self, state_idx):
        row, col = self.find_coord(0,state_idx) #get row, col of blank
        
        moves = []
        if col > 0:
            moves.append((row, col - 1))    #go left
        if row > 0:
            moves.append((row - 1, col))    #go up
        if row < 2:
            moves.append((row + 1, col))    #go down
        if col < 2:
            moves.append((row, col + 1))    #go right
        return moves

    #Generates all child states for the state indexed by state_idx
    #in state_lst.  Appends child states to the list
    def depth_first(self,state_idx,level,goal):
        closed = []
        #finds where we're getting the location
        where = len(self.state_lst)-1
        #get legal moves
        move_lst = self.get_new_moves(where)
        #blank is a tuple, holding coordinates of the blank tile
        blank = self.find_coord(0,where)
        #where the is a move to be checked and we are not deeper than 5
        while move_lst or level < 5:
                
            #tile is a tuple, holding coordinates of the tile to be swapped
            #with the blank
            for tile in move_lst:
            #create a new state using deep copy 
            #ensures that matrices are completely independent
                child = deepcopy(self.state_lst[state_idx])

                #move tile to position of the blank
                child[blank[0]][blank[1]] = child[tile[0]][tile[1]]

                #set tile position to 0                          
                child[tile[0]][tile[1]] = 0
                #will not add the child if it is already in the state list or closed
                if child not in self.state_lst and child not in closed:
                    self.state_lst.append(child)
                    #checks to see if the child is the goal, if yes returns ture
                    if child == goal:
                        return True
                    else: 
                        #removes the current list from the moves list
                        cur = move_lst.pop()
                        #pushes child onto the closed list
                        closed.append(child)
                        #recursive call
                        self.depth_first(len(self.state_lst)-1,level + 1, goal)
                        return True     
        return False

def main():
    #nested list representation of 8 puzzle. 0 is the blank.
    #This configuration is found on slide 8, E: Two Search Algorithms
    parent = [[2,8,3],
              [1,6,4],
              [7,0,5]]
    
    goal = [[1,2,3],
            [8,0,4],
            [7,6,5]]

    level = 0  

    #initialize the list of states (state_lst) with the parent
    p = EightPuzzle(parent)
  
    #Generate the states reachable from the parent, i.e., 0th state in state_lst
    
    p.depth_first(0,level,goal)

    #display all states in state_lst                    
    p.display()
   

main()

