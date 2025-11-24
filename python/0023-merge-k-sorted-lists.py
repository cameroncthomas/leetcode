# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class HeapNode:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other_heap_node):
        return self.node.val < other_heap_node.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Idea:
        # - Brute force approach
        # Gather all nodes into array, sort array by node val, iterate and update
        # ptrs, return resultant linked list.
        # TC: O(N * log N), SC: O(N), where N is total num of nodes.
        # - Sub-optimal approaches
        # Two ways: 1) Iterate through lists array, merging lists together using a
        # merge_two_lists(list1, list2) helper function.
        # 2) Scan lists array and find node with smallest val each iteration,
        # updating ptrs accordingly. Return merged list.
        # TC: O(N * k), SC: O(1), where k = len(lists) is num of linked lists.
        # - Optimal approach
        # Use min_heap to efficiently select node with smallest val each loop.
        # Heapify array of linked lists, and keep popping from heap and updating ptrs.
        # TC: O(N * log(k)), since we are popping from a heap of size k, N many times.
        # SC: O(k) from the min_heap array.

        if not lists:
            return None

        dummy = ListNode()
        tail = dummy

        min_heap = [HeapNode(lst) for lst in lists if lst]
        heapify(min_heap)

        while min_heap:
            curr_min_heap_node = heappop(min_heap)
            tail.next = curr_min_heap_node.node
            tail = tail.next

            if curr_min_heap_node.node.next:
                heappush(min_heap, HeapNode(curr_min_heap_node.node.next))

        return dummy.next
