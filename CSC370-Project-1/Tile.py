import numpy as np

class Tile:
    
    def __init__(self, array = []):
        self.traveled = 0
        self.expected = 0
        
        if len(array) == 0:
            arr = np.arange(9)
            arr = np.random.permutation(arr)
            self.array = arr.reshape((3,3))
        
            #If not solvable, then simply exchange two first non-zero tiles to flip parity. Makes it solvable.
            if not self.hasSolution():
                for x in range(3):
                    for y in range(3):
                        if self.array[x][y] != 0:
                            for i in range(x,3):
                                for j in range(y,3):
                                    if self.array[i][j] != 0:
                                        self.array[x][y],self.array[i][j] = self.array[i][j],self.array[x][y]

        else:
            self.array = array
            
    
    def __lt__(self, other):
        return self.expected < other.expected
            
    def generateFrontier(self):
        res = []
        
        for x in range(3):
            for y in range(3):
                if self.array[x][y] == 0:
                    index = (x,y)
    
        x = index[0]
        y = index[1]
        
        if x > 0:
            temp = self.array.copy()
            tempVal = self.array[x-1][y]
            temp[x][y] = tempVal
            temp[x-1][y] = 0
            res.append(Tile(temp))
        if y > 0:
            temp = self.array.copy()
            tempVal = self.array[x][y-1]
            temp[x][y] = tempVal
            temp[x][y-1] = 0
            res.append(Tile(temp))
        if x < 2:
            temp = self.array.copy()
            tempVal = self.array[x+1][y]
            temp[x][y] = tempVal
            temp[x+1][y] = 0
            res.append(Tile(temp))
        if y < 2:
            temp = self.array.copy()
            tempVal = self.array[x][y+1]
            temp[x][y] = tempVal
            temp[x][y+1] = 0
            res.append(Tile(temp))
        return res
    
    def hasSolution(self) -> bool:
        #according to https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
        arr = self.array.flatten()
        inversions = 0
        for i in range(9):
            for j in range(i,9):
                if arr[j] < arr[i] and arr[j] != 0:
                    inversions += 1
        if inversions % 2 == 0:
            return True
        return False
    
    def isSolution(self) -> bool:
        return np.array_equal(self.array, np.array([[1,2,3],[4,5,6],[7,8,0]]))
    
                

