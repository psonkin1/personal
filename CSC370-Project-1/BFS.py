import Tile as tl
import collections as cols
import numpy as np

def randomBFS():
    visited = set()
    frontier = cols.deque([tl.Tile(np.array([[1,2,3],[4,5,6],[7,8,0]]))])
    curDepth = 0
    counter = 0
    
    f = open("SolvableTiles.txt", 'r')
    f.close()
    
    while(curDepth < 25):
        #Peek at left
        
        tile = frontier[0]
        
        #If new depth reached
        if tile.traveled > curDepth:
            curDepth = tile.traveled
            #Close file
            f.close()
            #Counter to 0
            counter = 0
            #upon change of depth, permute deque
            permuter = np.random.permutation(frontier)
            frontier = cols.deque(permuter)
            
            #If new, even depth, create new file.
            if tile.traveled % 2 == 0:
                f= open(str(tile.traveled) + "solvable.txt","w+")
                
        tile = frontier.popleft()
        print(tile.array)
        print(tile.traveled)
        visited.add(hash(tile.array.tobytes()))
        
        
        if not f.closed and counter < 100:
            temp = list(tile.array.reshape(9))
            f.write(str(temp))
            f.write('\n')
            counter += 1
        
        neibs = tile.generateFrontier()
        
        for n in neibs:
            if (hash(n.array.tobytes()) not in visited):
                n.traveled = tile.traveled + 1
                frontier.append(n)
        
def main():
    randomBFS()
    
main()