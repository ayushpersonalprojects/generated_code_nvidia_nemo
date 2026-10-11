# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        """
        :type root: List[int] or TreeNode
        :rtype: List[int]
        """
        # Helper to build tree from level-order list (with None for missing nodes)
        def list_to_tree(lst):
            if not lst:
                return None
            root_node = TreeNode(lst[0])
            queue = [root_node]
            i = 1
            while queue and i < len(lst):
                node = queue.pop(0)
                if lst[i] is not None:
                    node.left = TreeNode(lst[i])
                    queue.append(node.left)
                i += 1
                if i < len(lst) and lst[i] is not None:
                    node.right = TreeNode(lst[i])
                    queue.append(node.right)
                i += 1
            return root_node

        # Helper to serialize tree to level-order list (without trailing None)
        def tree_to_list(root_node):
            if not root_node:
                return []
            result = []
            queue = [root_node]
            while queue:
                node = queue.pop(0)
                if node:
                    result.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    result.append(None)
            # Trim trailing None values
            while result and result[-1] is None:
                result.pop()
            return result

        # If input is a list, convert to TreeNode, invert, then convert back to list
        if isinstance(root, list):
            tree_root = list_to_tree(root)
            # Invert the tree recursively
            def invert(node):
                if not node:
                    return
                node.left, node.right = node.right, node.left
                invert(node.left)
                invert(node.right)
            invert(tree_root)
            return tree_to_list(tree_root)
        else:
            # Input is already a TreeNode; invert and return the same root (as TreeNode)
            def invert(node):
                if not node:
                    return
                node.left, node.right = node.right, node.left
                invert(node.left)
                invert(node.right)
            invert(root)
            return root