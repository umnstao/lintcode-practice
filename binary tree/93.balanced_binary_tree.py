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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        a, b = self.helper(root)
        return b

    def helper(self,root):
        if root is None:
            return 0, True
        leftDepth, leftCond = self.helper(root.left)
        rightDepth, rightCond = self.helper(root.right)
        if leftCond is False or rightCond is False:
            return 0, False
        if abs(leftDepth - rightDepth) > 1:
            return 0, False
        else:
            return max(leftDepth, rightDepth) + 1, True



