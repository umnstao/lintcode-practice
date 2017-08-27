"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum2(self, root, target):
        # Write your code here
        if not root:
            return []
        ret = []
        self.pathSum(root,target,ret)
        return ret

    def pathSum(self,root,target, ret):
        if not root:
            return None
        path = []
        self.maxPathSumFrom(root, target, ret, path)
        #print ret
        if root.left:
            self.pathSum(root.left, target, ret)
        if root.right:
            self.pathSum(root.right, target, ret)

    def maxPathSumFrom(self, root, target, ret, path):
        path = path + [root.val]
        if root.val == target:
            ret.append(path[:])
        if root.left:
            self.maxPathSumFrom(root.left, target - root.val, ret, path)
        if root.right:
            self.maxPathSumFrom(root.right, target - root.val, ret, path)

    # traversal
