"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        if root is None:
            return []
        ret = []
        self.helper(root,ret,""+str(root.val))
        return ret

    def helper(self,root, ret, path):
        if root.left is None and root.right is None:
            ret.append(path)
        if root.left:
            self.helper(root.left, ret, path +'->'+str(root.left.val) )
        if root.right:
            self.helper(root.right, ret, path + '->'+ str(root.right.val))
