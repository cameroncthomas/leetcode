class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Idea:
        # Sort nums array and iterate through nums with 3 ptrs.
        # For each num in nums, initialise two ptrs, one to right of num, one at end of
        # nums array. Then use two ptr approach (as in TwoSumII) to find triplets.
        # Take care of duplicates by checking if curr val is same as prev val.
        # TC: O(n log n + n^2) = O(n^2).
        # SC: triplets arr does not contribute but sorting algo (Powersort) is O(n).

        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1

        return triplets
