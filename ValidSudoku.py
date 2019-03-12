class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(grid):
            for i in grid:
                mySet=set()
                for j in i:
                    if j is '.':
                        pass
                    elif j in mySet:
                        return False
                    mySet.add(j)
            
        def checkCol(grid):
            for i in range(9):
                mySet=set()
                for j in range(9):
                    if grid[j][i] is '.':
                        pass
                    elif grid[j][i] in mySet:
                        return False
                    mySet.add(grid[j][i])
        
        def checkGrid(grid):
            starts=[[0,1,2],[3,4,5],[6,7,8]]
        
            for i in starts:
                for j in starts:
                    mySet=set()
                    for x in i:
                        for y in j:
                            if grid[x][y] is '.':
                                pass
                            elif grid[x][y] in mySet:
                                return False
                            mySet.add(grid[x][y])        
    
        if checkRow(board) is False:
            return False
        if checkCol(board) is False:
            return False
        if checkGrid(board) is False:
            return False
        return True
