from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int,
                 left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: List[Optional[int]]) -> List[List[int]]:
        # Build tree from level-order list (with None for missing nodes)
        if not root or root[0] is None:
            return []

        nodes = [None if v is None else TreeNode(v) for v in root]
        child_iter = iter(nodes[1:])
        for node in nodes:
            if node is None:
                continue
            try:
                node.left = next(child_iter)
            except StopIteration:
                break
            try:
                node.right = next(child_iter)
            except StopIteration:
                break

        tree_root = nodes[0]

        # Standard BFS to collect values by depth
        result: List[List[int]] = []
        q = deque([tree_root])
        while q:
            level_size = len(q)
            level_vals: List[int] = []
            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.val)  # node is guaranteed not None here
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level_vals)
        return result