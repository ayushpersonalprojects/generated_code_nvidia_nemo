import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # Check if the input is a list of lists (needs conversion to linked lists)
        if isinstance(lists[0], list):
            linked_lists = []
            for lst in lists:
                if not lst:
                    linked_lists.append(None)
                else:
                    head = ListNode(lst[0])
                    curr = head
                    for i in range(1, len(lst)):
                        curr.next = ListNode(lst[i])
                        curr = curr.next
                    linked_lists.append(head)
        else:
            linked_lists = lists
        
        heap = []
        for i, node in enumerate(linked_lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        curr = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next