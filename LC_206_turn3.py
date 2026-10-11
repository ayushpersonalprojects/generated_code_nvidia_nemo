# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        """
        Reverses a singly linked list or a list of values.
        If head is a list, returns a reversed list.
        If head is a ListNode, returns the new head of the reversed linked list.
        """
        if isinstance(head, list):
            # Return a new list with elements in reverse order
            return head[::-1]
        
        # Otherwise, treat head as a ListNode (or None)
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev