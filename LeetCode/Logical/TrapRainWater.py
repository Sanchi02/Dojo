# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i,h in enumerate(height):
            left_max = max(height[:i+1])
            right_max = max(height[i:])
            tmp = min(left_max, right_max) - h
            # print("Left_max = {} right_max={} tmp = {}".format(left_max,right_max,tmp))
            water += tmp
        return water