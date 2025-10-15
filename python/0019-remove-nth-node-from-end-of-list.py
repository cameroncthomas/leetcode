# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Idea:
        # Create dummy node whose next ptr points to head.
        # Initialise two ptrs, first and second, at dummy node.
        # Iterate second ptr until ahead of first ptr by n nodes.
        # Then iterate both ptrs until second ptr is at last node.
        # At this point, first.next will point to node to be removed.
        # Remove node from list by setting first.next = first.next.next.
        # Return dummy.next.
        # TC: one-pass O(L), where L is num nodes in head.
        # SC: O(1)

        dummy = ListNode(val=0, next=head)
        first, second = dummy, dummy

        for _ in range(n):
            second = second.next

        while second.next is not None:
            first = first.next
            second = second.next

        first.next = first.next.next

        return dummy.next
