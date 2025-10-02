class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Idea:
        # - Brute force approach
        # Iterate through both lists in sorted fashion until half of all elements
        # has been reached and then return median.
        # TC: O(m + n), where m, n are the lengths of nums1, nums2 respectively.
        # SC: O(1)
        # - Optimal approach
        # Binary search the smaller array to find the correct median value.
        # Since both arrays are sorted, we can check if we have chosen the correct
        # value by comparing the next values along in the arrays.
        # If our partition is incorrect (vals in smaller array are too big or
        # too small), then update the binary search ptrs accordingly.
        # Turning to our algorithm, we find the idxs in both arrays of the vals
        # that are just to the left of the median. Then we pick out the median
        # from the next val across (either by choosing min or taking average).
        # Since we are looking at the next val across, our array idxs may be out
        # of range by 1. To handle this, set the val of the array element to
        # be ± infinity if the idx is too big or too small respectively.
        # We must also initialise the left binary search ptr to be -1 for this reason.
        # TC: O(log(min(m,n))), since we binary search on the smaller array.
        # SC: O(1)

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        total = len(nums1) + len(nums2)
        half = total // 2

        left, right = -1, len(nums1) - 1
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = half - mid1 - 2

            nums1_left = nums1[mid1] if mid1 >= 0 else -float("inf")
            nums1_right = (
                nums1[mid1 + 1] if mid1 + 1 <= len(nums1) - 1 else float("inf")
            )
            nums2_left = nums2[mid2] if mid2 >= 0 else -float("inf")
            nums2_right = (
                nums2[mid2 + 1] if mid2 + 1 <= len(nums2) - 1 else float("inf")
            )

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2 != 0:
                    return min(nums1_right, nums2_right)
                else:
                    return (
                        max(nums1_left, nums2_left) + min(nums1_right, nums2_right)
                    ) / 2
            elif nums1_left > nums2_right:
                right = mid1 - 1
            else:
                left = mid1 + 1
