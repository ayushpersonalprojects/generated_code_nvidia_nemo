# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    """
    Returns True if the linked list has a cycle, otherwise False.
    Uses Floyd's Tortoise and Hare algorithm (O(1) space, O(n) time).
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next          # move one step
        fast = fast.next.next     # move two steps
        if slow is fast:          # meeting point indicates a cycle
            return True
    return False