"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
import copy
class Solution:
    """
    @param {TreeNode} root The root of the binary tree.
    @param {TreeNode} A and {TreeNode} B two nodes
    @return Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        aExist, bExist, lca = self.helper(root, A, B)
        if aExist and bExist:
            return lca
        else:
            return None

    def helper(self, root, A, B):
        # exit
        if root is None:
            return False, False, None
        # divide
        aLeft, bLeft, lcaLeft = self.helper(root.left, A, B)
        aRight, bRight, lcaRight = self.helper(root.right, A, B)
        aExist = aLeft or aRight or root == A
        bExist = bLeft or bRight or root == B
        # solve
        if root == A or root == B:
            return aExist, bExist, root
        if lcaLeft and lcaRight:
            return aExist, bExist, root
        if lcaLeft is None and lcaRight is not None:
            return aExist, bExist, lcaRight
        if lcaLeft is not None and lcaRight is None:
            return aExist, bExist, lcaLeft

        return aExist, bExist, None
        # divide and conquer, bottom up

