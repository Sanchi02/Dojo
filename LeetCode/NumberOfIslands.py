# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if(rows==0):
            return 0
        cols = len(grid[0])
        ctr = 0
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == "1"):
                    ctr += 1
                    self.mark(grid,i,j,rows,cols)
        print(grid)
        return ctr
                
    def mark(self,grid,i,j,rows,cols):
        if(j+1<cols):
            if(grid[i][j+1]=="1"):
                grid[i][j+1]="S"
                self.mark(grid,i,j+1,rows,cols)
        if(j-1>=0):
            if(grid[i][j-1]=="1"):
                grid[i][j-1]="S"
                self.mark(grid,i,j-1,rows,cols)
        if(i+1<rows):
            if(grid[i+1][j]=="1"):
                grid[i+1][j]="S"
                self.mark(grid,i+1,j,rows,cols)
        if(i-1>=0):
            if(grid[i-1][j]=="1"):
                grid[i-1][j]="S"
                self.mark(grid,i-1,j,rows,cols)