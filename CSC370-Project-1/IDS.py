import numpy as np
import Tile as tl
import heapq as hq
import heuristics as hs
import collections as cols
from ast import literal_eval



def IDS(tile):
    #This IDS is informed :)) big brain IDS still slow af 
    totalNodes = 0
    for depthMax in range(2,25,2):
        searchRes = DFS(tile,depthMax)
        totalNodes += searchRes[1]
        if searchRes[0]:
            return totalNodes
        
    print("ss")
    return 0



def DFS(tile, depthMax):
    frontier = cols.deque([tile])
    visited = set()
    totalNodes = 0
    
    while(True):
        if len(frontier) == 0:
            return (False,totalNodes)
        temp = frontier.pop()
        if temp.isSolution():
            return (True,totalNodes)
        if temp.traveled < depthMax: 
            neibs = temp.generateFrontier()
            for n in neibs:
                totalNodes += 1
                if hash(n.array.tobytes()) not in visited:
                    visited.add(hash(n.array.tobytes()))
                    n.traveled = temp.traveled + 1
                    frontier.append(n)
     
            
    

def main(files):
    for file in files:
        print(file)
        nodes = 0
        differentProbs = 0
        f = open(file, 'r')
        f1 = f.readlines()
        line_count = 0
        for line in f1:
            
            differentProbs +=1
            arr = np.array(literal_eval(line)).reshape((3,3))
            res = IDS(tl.Tile(arr))
            if(res == 0):
                print("failed to find sol at: ", line_count)
            nodes += res
            line_count += 1
        #print(differentProbs)
        print(nodes//differentProbs)
        
#main(["2solvable.txt","4solvable.txt","6solvable.txt","8solvable.txt","10solvable.txt","12solvable.txt","14solvable.txt","16solvable.txt","18solvable.txt" ])
main(["2solvable.txt","4solvable.txt","6solvable.txt","8solvable.txt","10solvable.txt","12solvable.txt"])
