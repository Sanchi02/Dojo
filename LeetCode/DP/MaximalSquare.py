# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4

# Input: matrix = [["0","1"],["1","0"]]
# Output: 1

# Input: matrix = [["0"]]
# Output: 0

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        nrows = len(matrix)
        ncols = len(matrix[0])
        max_square_len = 0
        dp = [[0] * (ncols + 1) for i in range(nrows + 1)]
        
        for i in range(1, nrows + 1):
            for j in range(1, ncols + 1):
                if (matrix[i - 1][j - 1] == '1'):
                    print("Value of (i-1,j-1) = ({},{})".format(i-1,j-1))
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    for t in range(nrows+1):
                        print(dp[t])
                    print("_________________________")
                    max_square_len = max(max_square_len, dp[i][j])
                    
        return max_square_len ** 2