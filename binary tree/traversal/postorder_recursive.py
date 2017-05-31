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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        return self.postorderTraversal(root.left) + \
        self.postorderTraversal(root.right) + [root.val]

    def postorderTraversal(self, root):
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
        self.helper(root.right,ret)
        ret.append(root.val)
