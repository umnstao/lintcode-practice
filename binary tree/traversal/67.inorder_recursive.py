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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] +\
        self.inorderTraversal(root.right)

    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        ret = []
        self.helper(root, ret)
        return ret

    def helper(self, root, ret):
        if not root:
            return

        self.helper(root.left,ret)
        ret.append(root.val)
        self.helper(root.right,ret)
