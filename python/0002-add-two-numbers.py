# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Idea:
        # Traverse through lists. Total up node vals and any carry from previous sum.
        # Since total may exceed 9, set current node val = total % 10 and keep track
        # of carry = total // 10. If node is None treat its val as zero.
        # TC: O(max(m,n)), where m and n are the lengths of l1 and l2 respectively.
        # SC: O(1), since size of output is not considered in analysis.

        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            val = total % 10
            carry = total // 10

            tail.next = ListNode(val)

            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
