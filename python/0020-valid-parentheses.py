class Solution:
    def isValid(self, s: str) -> bool:
        # Idea:
        # Use hashmap to map closing brackets to their corresponding opening type.
        # Use stack and iterate through s.
        # Now, conditionally check if string is valid. There are many different ways
        # we could implement this, but in every case we must check if there is a:
        # 1) Closing bracket appearing with no opening bracket in stack.
        # 2) Closing bracket of different type to most recent opening bracket in stack.
        # Where we return False in either case.
        # Otherwise, we'll append the ch to stack if of opening type and pop from stack
        # if of correct closing type.
        # If s is valid, then stack should be empty after completing loop through s.
        # TC: one-pass O(n), SC: O(n), where n is length of s.

        close_to_open = {")": "(", "}": "{", "]": "["}
        stack = []

        for ch in s:
            if ch not in close_to_open:
                stack.append(ch)

            elif stack and close_to_open[ch] == stack[-1]:
                stack.pop()

            else:
                return False

        return len(stack) == 0
