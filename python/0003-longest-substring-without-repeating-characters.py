class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Idea:
        # Sliding window with a ch_freq hashmap.
        # Keep increasing window until repeated ch detected.
        # While ch freq is > 1, decrease window and corresponding ch freq.
        # Keep track of max window size.
        # TC: O(2*n) in the worst case, so O(n), where n is the size of s.
        # SC: O(size of ch_freq hashmap) = O(num_unique_chs_in_s). In terms of
        # the size of charset, m, and size of s, n, this is O(min(m,n)).

        if s == "":
            return 0

        ch_freq = defaultdict(int)
        max_length = 0
        left, right = 0, 0

        while right < len(s):
            ch_freq[s[right]] += 1

            while ch_freq[s[right]] > 1:
                ch_freq[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length
