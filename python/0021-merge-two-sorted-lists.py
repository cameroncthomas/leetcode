# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Idea:
        # Use dummy node and tail ptr. Iterate through list1 and list2, comparing node vals.
        # Since lists may be of diff length, set node val to +inf if node is None.
        # Set tail.next to node with lower or same val and update list ptrs.
        # Can also handle edge case of one or both lists initially being empty.
        # Return dummy.next.
        # TC: O(n1 + n2), where n1, n2 are num nodes in list1, list2 respectively.
        # SC: O(1)

        if not list1 or not list2:
            return list1 or list2

        dummy = ListNode()
        tail = dummy

        while list1 or list2:
            val1 = list1.val if list1 else float("inf")
            val2 = list2.val if list2 else float("inf")

            if val1 <= val2:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        return dummy.next
