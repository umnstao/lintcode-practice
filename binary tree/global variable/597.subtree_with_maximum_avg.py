"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    maxAvg = -float('inf')
    maxRoot = None
    def findSubtree2(self, root):
        self.helper(root)
        return self.maxRoot

    def helper(self, root):
        if root is None:
            return 0, 0
        leftSum, leftNum = self.helper(root.left)
        rightSum, rightNum = self.helper(root.right)
        localSum = leftSum + rightSum + root.val
        localNum = leftNum + rightNum + 1
        localAvg = 1.0*localSum/localNum
        if localAvg > self.maxAvg:
            self.maxAvg = localAvg
            self.maxRoot = root
        return localSum, localNum

        # divide and conquer, bottom-up