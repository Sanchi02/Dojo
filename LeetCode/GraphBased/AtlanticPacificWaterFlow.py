# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

# Example 1:


# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Example 2:

# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]
 

# Constraints:

# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights),len(heights[0])
        pacific, atlantic = set(),set()
        res = []
        
        def dfs(r,c,visited,prevHeight):
            if((r,c) in visited or r>rows-1 or c>cols-1 or r<0 or c<0 or heights[r][c]<prevHeight):
                return
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            
        for i in range(rows):
            dfs(i,0,pacific,heights[i][0])
            dfs(i,cols-1,atlantic,heights[i][cols-1])
            
        for i in range(cols):
            dfs(0,i,pacific,heights[0][i])
            dfs(rows-1,i,atlantic,heights[rows-1][i])
            
        for i in range(rows):
            for j in range(cols):
                if((i,j) in pacific and (i,j) in atlantic):
                    res.append((i,j))
        
        return res
        
                