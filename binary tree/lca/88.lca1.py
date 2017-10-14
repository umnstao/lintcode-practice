"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here

        if not root:
            return None
        if root == A or root == B:
            return root
        lcaLeft = self.lowestCommonAncestor(root.left, A, B)
        lcaRight = self.lowestCommonAncestor(root.right, A, B)

        if lcaLeft is not None and lcaRight is not None:
            return root
        if lcaLeft is not None and lcaRight is None:
            return lcaLeft
        if lcaLeft is None and lcaRight is not None:
            return lcaRight
        return None

        # divide and conquer, bottom-up



