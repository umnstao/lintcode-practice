"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the minimum subtree
    minSum = float('inf')
    minRoot = None
    def findSubtree(self, root):
        self.helper(root)
        return self.minRoot

    def helper(self,root):
        if not root:
            return 0
        leftSum = self.helper(root.left)
        rightSum = self.helper(root.right)
        localSum = leftSum + rightSum + root.val
        if localSum < self.minSum:
            self.minSum = localSum
            self.minRoot = root
        return localSum