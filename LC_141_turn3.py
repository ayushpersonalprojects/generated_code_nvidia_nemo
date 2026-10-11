# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, *args, **kwargs):
        head = None
        if args:
            head = args[0]
        else:
            if 'values' in kwargs:
                values = kwargs['values']
                pos = kwargs.get('pos', -1)
                if values is None or len(values) == 0:
                    return False
                nodes = [ListNode(val) for val in values]
                for i in range(len(nodes) - 1):
                    nodes[i].next = nodes[i+1]
                if pos != -1 and pos < len(nodes):
                    nodes[-1].next = nodes[pos]
                head = nodes[0]
            elif 'head' in kwargs:
                head = kwargs['head']
            else:
                return False
        
        if head is None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False