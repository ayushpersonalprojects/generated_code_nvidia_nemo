# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root) -> int:
        # Helper to build tree from level-order list (with None for missing nodes)
        def build_tree(vals):
            if not vals:
                return None
            nodes = [None if v is None else TreeNode(v) for v in vals]
            child_idx = 1
            for i, node in enumerate(nodes):
                if node is None:
                    continue
                if child_idx < len(nodes):
                    node.left = nodes[child_idx]
                    child_idx += 1
                if child_idx < len(nodes):
                    node.right = nodes[child_idx]
                    child_idx += 1
            return nodes[0]

        # If input is a list, convert to TreeNode; otherwise assume it's already a TreeNode
        if isinstance(root, list):
            root = build_tree(root)

        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            current = node.val + left + right
            self.max_sum = max(self.max_sum, current)
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum