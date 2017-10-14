"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree.
    @return: An integer
    """
    def maxPathSum2(self, root):
        # write your code here
        if not root:
            return -float('inf')

        return root.val + max(0,max(self.maxPathSum2(root.left), self.maxPathSum2(root.right)))

    # divide and conquer
