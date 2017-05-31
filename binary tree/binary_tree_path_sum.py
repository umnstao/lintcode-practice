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
    def binaryTreePathSum(self, root, target):
        # Write your code here
        if not root:
            return []
        ret = []
        path = [root.val]
        self.helper(root, ret, path, target, root.val)
        return ret

    def helper(self, root, ret, path, target, sums):
        if root.left is None and root.right is None:
            if sums == target:
                ret.append(path)
        if root.left:
            self.helper(root.left,ret,path+[root.left.val],target,sums+root.left.val)

        if root.right:
            self.helper(root.right,ret,path+[root.right.val],target,sums+root.right.val)
