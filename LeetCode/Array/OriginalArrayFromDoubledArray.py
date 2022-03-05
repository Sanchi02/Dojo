# https://leetcode.com/problems/find-original-array-from-doubled-array/
# An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

# Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

 

# Example 1:

# Input: changed = [1,3,4,2,6,8]
# Output: [1,3,4]
# Explanation: One possible original array could be [1,3,4]:
# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.
# Other original arrays could be [4,3,1] or [3,1,4].
# Example 2:

# Input: changed = [6,3,0,1]
# Output: []
# Explanation: changed is not a doubled array.
# Example 3:

# Input: changed = [1]
# Output: []
# Explanation: changed is not a doubled array.
 

# Constraints:

# 1 <= changed.length <= 105
# 0 <= changed[i] <= 105


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        """
        The idea is to:
            1st sort the numbers
            2nd Create a counter to save the frequency of each number
            3nd iterate the array and for each number check if the double exists.
            4rd after taking len(changed) // 2 numbers return the answer
            
        Time complexity: O(nlog(n)) 
        Space complexity: O(n)
        
        """
        
        
        if len(changed) % 2 != 0: # If there are not even amount the numbers there is no solution.
            return []
        
        changed.sort()
        
        c = Counter(changed) # The counter is needed because we have 0s
        
        answer = []
        for num in changed:
            # print(c)
            if num in c and c[num] >= 1: # Check if the number is available (we may have taken it before)
                c[num] -= 1 # we mark the number as used by decreasing the counter (only needed for the zeros)
                if (num * 2) in c and c[(num * 2)] >= 1: # Take the one that doubles it if exists
                    answer.append(num)
                    c[num*2] -= 1 # The number has been taken.
            
            if len(answer) == len(changed) // 2:
                return answer
        
        return []