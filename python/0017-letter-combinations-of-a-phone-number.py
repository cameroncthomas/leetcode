class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Idea:
        # Map each digit to its letters in digit_to_letters hashmap.
        # Define a backtrack inner function with digits idx as arg.
        # For each letter in digit_to_letters[digit], append letter to current
        # combination then recursively call backtrack function on next digit.
        # Remember to pop from current combination after recursive backtrack call.
        # TC: O(total_num_of_combinations * len(comb)) =
        # O(max_num_letters_associated_with_digit^n * n) =
        # O(4^n * n), where n is length of digits.
        # SC: O(n) from comb array.

        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combs = []
        comb = []

        def backtrack(i):
            if i == len(digits):
                combs.append("".join(comb))
                return None

            for ch in digit_to_letters[digits[i]]:
                comb.append(ch)
                backtrack(i + 1)
                comb.pop()

            return None

        backtrack(0)

        return combs
