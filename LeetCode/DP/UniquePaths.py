# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?


# Above is a 7 x 3 grid. How many possible unique paths are there?

 

# Example 1:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:

# Input: m = 7, n = 3
# Output: 28
 

# Constraints:

# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n]*m
        tmp = self.recur(grid,0,0,m,n,0)
        return tmp
        
    def recur(self,grid,i,j,m,n,tot):
        # print("Val of i = {}, j={}".format(i,j))
        if(i==m-1 or j==n-1):
            grid[i][j] = 1
            return grid[i][j]
        if(i<m-1 and j<n-1):
            if(grid[i+1][j]>0):
                grid[i][j] = grid[i+1][j] + self.recur(grid,i,j+1,m,n,tot)
            elif(grid[i][j+1]>0):
                grid[i][j] = self.recur(grid,i+1,j,m,n,tot) + grid[i][j+1]
            else:
                grid[i][j] = self.recur(grid,i+1,j,m,n,tot) + self.recur(grid,i,j+1,m,n,tot)
            return grid[i][j]
        if(i<m-1):
            return grid[i+1,j]
        if(j<n-1):
            return grid[i,j+1]
        