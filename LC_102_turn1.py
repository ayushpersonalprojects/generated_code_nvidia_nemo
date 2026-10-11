from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def group_by_depth(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        level_size = len(q)
        level_vals = []
        for _ in range(level_size):
            node = q.popleft()
            level_vals.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level_vals)
    return result