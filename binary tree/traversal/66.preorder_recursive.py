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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        ret = []
        self.helper(root, ret)
        return ret

    def helper(self, root, ret):
        if not root:
            return
        ret.append(root.val)
        self.helper(root.left, ret)
        self.helper(root.right, ret)
