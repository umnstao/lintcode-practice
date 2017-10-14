"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing

    def flatten(self, root):
        if not root:
            return None

        self.flatten(root.left)
        self.flatten(root.right)

        right = root.right
        root.right = root.left
        root.left = None
        cur = root
        while cur.right:
            cur = cur.right
        cur.right = right
