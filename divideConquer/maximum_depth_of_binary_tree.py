"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        return self.helper(root)
    def helper(self, root):
        if root is None:
            return 0
        leftDepth = self.helper(root.left)
        rightDepth = self.helper(root.right)
        return max(leftDepth, rightDepth) + 1