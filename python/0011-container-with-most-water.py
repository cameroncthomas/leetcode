class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Idea:
        # - Brute force approach
        # Calculate all areas whilst keeping track of max_area. Return max_area.
        # TC: O(n^2) where n is length of height array, SC: O(1).
        # - Optimal approach
        # Greedy algo with two pointers.
        # Initialise pointers at either end of height array. Then update pointer
        # corresponding to smaller height. This opens up possibility of achieving
        # a larger current area and so is locally optimal.
        # Keep track of max_area and then return max_area.
        # TC: one-pass O(n), SC: O(1).

        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
