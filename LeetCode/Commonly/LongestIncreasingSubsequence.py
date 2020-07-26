class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        if(l==0):
            return 0
        dp = [1]*l
        # ptr = 0
        for i in range(l):
            ptr = 0
            while(ptr<i):
                if(nums[ptr]<nums[i] and dp[i]<=dp[ptr]):
                    dp[i] = dp[ptr] + 1
                ptr += 1
        return max(dp)