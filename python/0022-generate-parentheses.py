class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Idea:
        # Backtrack to build valid combs. Keep track of num open and closed parentheses.
        # If num of open parentheses < n, append '(' to current comb.
        # If num of closed parentheses < num of open parentheses, append ')' to comb.
        # When n pairs of parentheses have been added, append combination to ans.
        # TC: Total num of valid and invalid combs is O(2^(2*n)) = O(4^n),
        # since can add either '(' or ')' for each char in a string of length 2*n.
        # Considering valid combs only, this is reduced to O( 4^n / (n * sqrt(n)) ).
        # And for each valid comb, we perform an O(len(comb)) = O(2*n) operation on it
        # in the base case. Therefore, the overall TC is O(2*n * 4^n / (n * sqrt(n))) =
        # O(4^n / sqrt(n)).
        # SC: O(2*n) = O(n) from current combination array.

        comb = []
        combs = []

        def backtrack(num_open, num_closed):
            if num_open == num_closed == n:
                combs.append("".join(comb))
                return None

            if num_open < n:
                comb.append("(")
                backtrack(num_open + 1, num_closed)
                comb.pop()
            if num_closed < num_open:
                comb.append(")")
                backtrack(num_open, num_closed + 1)
                comb.pop()

            return None

        backtrack(0, 0)

        return combs
