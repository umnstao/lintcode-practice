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
    def minDepth(self, root):
        # write your code here

        if not root:
            return 0
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return float('inf')
        if root.left is None and root.right is None:
            return 1
        return min(self.helper(root.left), self.helper(root.right))+1

