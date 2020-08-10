class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        tracker = []
        val, deg = 0,0
        arr = set(nums)
        for ind,n in enumerate(arr):
            tmp = nums.count(n)
            if(tmp>=deg):
                if(tmp==deg):
                    tracker.append((n,tmp))
                else:
                    tracker = [(n,tmp)]
                val,deg = n,tmp
        minLen = len(nums)     
        for val,deg in tracker:
            leftPtr = nums.index(val)
            rightPtr = len(nums)-nums[::-1].index(val)-1
            # print("val = {}, deg = {}, leftPtr={}, rightPtr = {}".format(val,deg,leftPtr, rightPtr))
            minLen = min(minLen,rightPtr-leftPtr+1)
        return minLen