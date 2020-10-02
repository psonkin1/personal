import numpy as np
import Tile as tl
import heuristics as hs
import heapq as hq
from ast import literal_eval
from timeit import default_timer as timer

def AStar(tile, heur):
    
    frontier = [tile]
    visited = set()
    totalNodes = 1
    
    while(True):
        if (len(frontier) == 0):
            print("error")
            return (0,0)
        tile = hq.heappop(frontier)
        visited.add(hash(tile.array.tobytes()))
        #totalNodes += 1
        if tile.isSolution():
            return (tile.traveled, totalNodes)
            #return (tile.traveled, len(list(visited)))
        neighbors = tile.generateFrontier()
       
        for n in neighbors:
            #totalNodes += 1
            if (hash(n.array.tobytes()) not in visited):
                totalNodes += 1
                n.traveled = tile.traveled + 1
                n.expected = n.traveled + heur(n.array)
                hq.heappush(frontier, n)
            
    

def main(files, heur):
    
    for file in files:
        print(file)
        nodes = 0
        differentProbs = 0
        f = open(file, 'r')
        f1 = f.readlines()
        bf = 0
        for line in f1:
            differentProbs +=1
            arr = np.array(literal_eval(line)).reshape((3,3))
            dist, temp = AStar(tl.Tile(arr), heur)
            nodes += temp
        
        print("Distance to goal is: ", dist)
        #print(differentProbs)
        avNodes = nodes//differentProbs
        print("Average nodes created is: ",avNodes)
        print("Branching factor is: ", hs.branchingFactor(avNodes, dist))

print("Misplaced")
start = timer()
main(["2solvable.txt","4solvable.txt","6solvable.txt","8solvable.txt","10solvable.txt","12solvable.txt","14solvable.txt","16solvable.txt","18solvable.txt","20solvable.txt","22solvable.txt","24solvable.txt" ],hs.misplaced)
end = timer()
print(end - start)  
print("Manhattan")
start = timer()
main(["2solvable.txt","4solvable.txt","6solvable.txt","8solvable.txt","10solvable.txt","12solvable.txt","14solvable.txt","16solvable.txt","18solvable.txt","20solvable.txt","22solvable.txt","24solvable.txt" ],hs.mhd)
end = timer()
print(end - start)
print("Linear Conflict")
start = timer()
main(["2solvable.txt","4solvable.txt","6solvable.txt","8solvable.txt","10solvable.txt","12solvable.txt","14solvable.txt","16solvable.txt","18solvable.txt","20solvable.txt","22solvable.txt","24solvable.txt" ],hs.linearConflict)
end = timer()
print(end - start)
            
    
    
    