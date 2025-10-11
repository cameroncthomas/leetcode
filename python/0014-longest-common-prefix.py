class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Idea:
        # Choose initial string in strs. Iterate through each ch in that string.
        # Then, for each of the other strings in strs, check the chs match.
        # If all the chs match then move to next ch in initial string.
        # If ch doesn't match in a string or idx is out of range, return prefix slice.
        # If loop through initial string is successful then return initial string.
        # TC: O(len(longest_common_prefix) * n) = O(len(smallest_string) * n) =
        # O(total_num_chs_in_strs), where n is length of strs array.
        # SC: O(1)

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i == len(strs[j]):
                    return strs[0][:i]

                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]
