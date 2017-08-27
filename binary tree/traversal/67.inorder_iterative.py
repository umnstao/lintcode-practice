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
        node = root
        stack = []
        inorder = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            inorder.append(node.val)
            node = node.right
        return inorder