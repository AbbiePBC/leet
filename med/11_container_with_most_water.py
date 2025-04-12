# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution:
    def maxArea(self, heights: list[int]) -> int:

        l_idx = 0
        r_idx = len(heights) - 1
        max_area = 0
        while r_idx > l_idx:
            area = min(heights[l_idx], heights[r_idx]) * (r_idx - l_idx)
            max_area = max(max_area, area)
            if heights[l_idx] < heights[r_idx]:
                l_idx += 1
            else:
                r_idx -= 1
        return max_area


# USING TWO POINTER ALGO

# Complexity:
# TIME
# We iterate through heights once, doing O(1) calculation
# => overall O(N)
# SPACE:
# Store a couple of extra variables, O(1)
