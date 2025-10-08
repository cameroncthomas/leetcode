class Solution:
    def romanToInt(self, s: str) -> int:
        # Idea:
        # Map Roman numeral symbols to their corresponding value using hashmap.
        # Scan through s. Since s is a valid Roman numeral, if next symbol along has
        # greater value than current symbol, subtract current symbol value from
        # running total, otherwise, add current symbol value to total.
        # TC: O(n), where n is the length of s.
        # (Note, since s is a valid Roman numeral, s has a max length of 15.)
        # SC: O(7) = O(1).

        sym_to_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s_as_int = 0

        for i in range(len(s)):
            if i < len(s) - 1 and sym_to_val[s[i]] < sym_to_val[s[i + 1]]:
                s_as_int -= sym_to_val[s[i]]
            else:
                s_as_int += sym_to_val[s[i]]

        return s_as_int
