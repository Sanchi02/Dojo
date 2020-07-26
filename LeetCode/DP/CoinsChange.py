# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        tracker = [0]*amount
        if (amount < 1):
            return 0;
        return self.backtrack(coins, amount, tracker);
        
    def backtrack(self,coins,amt,tracker):
        if(amt<0):
            return -1
        if(amt==0):
            return 0
        if(tracker[amt-1]!=0):
            return tracker[amt-1]
        mini = 99999
        for c in coins:
            res = self.backtrack(coins, amt-c, tracker)
            if(res>=0 and res<mini):
                mini = 1 + res
        if(mini==99999):
            tracker[amt-1] = -1
        else:
            tracker[amt-1] = mini
        return tracker[amt-1]
