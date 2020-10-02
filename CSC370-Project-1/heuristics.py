import numpy as np
import Tile as tl
import math


def misplaced(board):
    goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
    misCount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != goal[i][j]:
                misCount += 1
    return misCount



mhdDict = {
    1:(0,0), 
     2:(0,1), 
     3:(0,2), 
     4:(1,0), 
     5:(1,1), 
     6:(1,2), 
     7:(2,0), 
     8:(2,1), 
     0:(2,2) 
}

def mhd(board):
    totalDist = 0
    for i in range(3):
        for j in range(3):
            goalIndex = mhdDict[board[i][j]]
            curIndex = (i,j)
            totalDist += abs(goalIndex[0] - curIndex[0]) + abs(goalIndex[1] - curIndex[1])
            
    return totalDist


#This feels stupid extra but idk... need to test for if goal is above,below,left,or right so...

def linearConflict(board):
    totalDist = 0
    for i in range(3):
        for j in range(3):
            #Still do manhattan
            goalIndex = mhdDict[board[i][j]]
            curIndex = (i,j)
            totalDist += abs(goalIndex[0] - curIndex[0]) + abs(goalIndex[1] - curIndex[1])
            
            #If on same horizontal as goal
            if curIndex[0] == goalIndex[0] and board[i][j]!=0:
                linPath = abs(goalIndex[1]-curIndex[1])

                #goal to right of cur
                if curIndex[1] < goalIndex[1]:
                    for x in range(1,linPath+1):
                        tempTile = board[i][j+x]
                        tempTileGoal = mhdDict[tempTile]
                        if tempTileGoal[0]== curIndex[0] and tempTileGoal[1] <= curIndex[1] and tempTile!=0:
                            totalDist+=1

                #goal to left of cur
                elif curIndex[1] > goalIndex[1]:
                    for x in range(1,linPath+1):
                        tempTile = board[i][j-x]
                        tempTileGoal = mhdDict[tempTile]
                        if tempTileGoal[0]== curIndex[0] and tempTileGoal[1] >= curIndex[1] and tempTile!=0:
                            totalDist+=1
            
            #If on same vertical as goal
            elif curIndex[1] == goalIndex[1] and board[i][j]!=0:
                linPath = abs(goalIndex[0]-curIndex[0])

                #goal below cur pos
                if curIndex[0] < goalIndex[0]:
                    for y in range(1,linPath+1):
                        #print(y)
                        tempTile = board[i+y][j]
                        tempTileGoal = mhdDict[tempTile]
                        if tempTileGoal[1]== curIndex[1] and tempTileGoal[0] <= curIndex[0] and tempTile!=0:
                            totalDist+=1

                #goal above cur pos
                elif curIndex[0] > goalIndex[0]:
                    for y in range(1,linPath+1):
                        tempTile = board[i-y][j]
                        tempTileGoal = mhdDict[tempTile]
                        if tempTileGoal[1]== curIndex[1] and tempTileGoal[0] >= curIndex[0] and tempTile!=0:
                            totalDist+=1
    return totalDist 

    

def branchingFactor(nodes, depth):
    low = 0
    hi = nodes ** (1/depth)
    counter = 0
    while low < hi and counter < 100:
        counter +=1 
        guess = (hi + low) / 2
        factor = 0
        for d in range(depth+1):
            factor += (guess**d / 1)
            
        if factor > nodes:
            hi = guess 
        else:
            low = guess
    return guess