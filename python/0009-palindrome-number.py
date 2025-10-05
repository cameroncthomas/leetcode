class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Idea:
        # - Sub-optimal approach
        # Convert x to string then check if palindrome using two ptrs.
        # TC: O(log(x)), SC: O(log(x)).
        # - Optimal approach
        # Use maths operations to build reversed number, then check if same as x.
        # Algo:
        # Starting from num = x, get last digit from num and add that to reversed_num.
        # Multiply reversed_num by 10 and remove last digit from num.
        # Keep doing this until all digits in x have been scanned (ie until num is zero).
        # Remove trailing zero from reversed_num (could add conditional in loop instead).
        # Check for edge case if x < 0. Can also cover if x is a non-zero multiple of 10.
        # TC: O(log(x)), SC: O(1).

        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        num = x
        reversed_num = 0

        while num > 0:
            reversed_num += num % 10
            reversed_num *= 10
            num //= 10

        reversed_num //= 10

        return x == reversed_num
