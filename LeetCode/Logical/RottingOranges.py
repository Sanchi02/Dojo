# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

# Example 1:



# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Note:

# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        fresh = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==2):
                    queue.append((i,j))
                elif(grid[i][j]==1):
                    fresh.append((i,j))
        ctr = 0
        print(queue)
        if(len(fresh)==0):
            return 0
        while(len(fresh)!=0 and ctr <100):
            for v in queue:
                if(v in fresh):
                    fresh.remove(v)
            queue = self.rotter(grid,queue)
            ctr += 1
            # print(ctr)
            # print(grid)
        if(ctr < 100):
            return ctr-1
        else:
            return -1
                
        
    def rotter(self, grid, queue):
        arr = []
        while(len(queue)!=0):
            val = queue.pop(0)
            x,y = val[0],val[1]
            if(x+1 < len(grid) and grid[x+1][y]!=2 and grid[x+1][y]==1):
                    grid[x+1][y]=2
                    arr.append((x+1,y))
            if(x-1 >= 0 and grid[x-1][y]!=2 and grid[x-1][y]==1):
                    grid[x-1][y]=2
                    arr.append((x-1,y))
            if(y+1 < len(grid[0]) and grid[x][y+1]!=2 and grid[x][y+1]==1):
                    grid[x][y+1]=2
                    arr.append((x,y+1))
            if(y-1 >=0 and grid[x][y-1]!=2 and grid[x][y-1]==1):
                    grid[x][y-1]=2
                    arr.append((x,y-1))
        queue = arr
        return queue
        