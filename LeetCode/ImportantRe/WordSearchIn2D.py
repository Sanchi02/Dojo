# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
 

# Constraints:

# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        for i in range(self.rows):
            for j in range(self.cols):
                if(self.checkAdj(i,j,word)):
                    return True
        return False
                    
    def checkAdj(self,i,j,suffix):
        if(len(suffix) == 0):
            return True
        if(i<0 or i==self.rows or j<0 or j==self.cols or self.board[i][j] !=suffix[0]):
            return False
        
        self.board[i][j] = '*'

        for r, c in [(0,1),(0,-1),(1,0),(-1,0)]:
            retVal = self.checkAdj(i+r, j+c,suffix[1:])
            if(retVal):
                break
        self.board[i][j] = suffix[0]
        return retVal
        
        