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
        if root is None:
            return 0
        leftDepth = self.helper(root.left)
        rightDepth = self.helper(root.right)
        return max(leftDepth, rightDepth) + 1


        ## divede and conquer, bottom up