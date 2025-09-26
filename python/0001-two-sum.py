class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Idea:
        # - Brute force approach
        # Calculate all possible pair sums using a nested for loop, checking to see if
        # pair sum equals target. Number of combinations is nC2 = n * (n - 1) / 2.
        # TC: O(n^2), SC: O(1)
        # - Optimal approach
        # Calculate diff required to reach target for each num in nums and check if diff
        # has previously been seen, returning indices if so. Store num and its index in
        # num_to_index hashmap as you iterate through nums.
        # TC: one-pass O(n), SC: O(n)

        num_to_index = {}

        for i in range(len(nums)):
            if (target - nums[i]) in num_to_index:
                return [num_to_index[target - nums[i]], i]

            num_to_index[nums[i]] = i

        return []
