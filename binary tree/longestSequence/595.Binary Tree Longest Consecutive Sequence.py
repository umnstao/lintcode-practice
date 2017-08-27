# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive(self, root):
        # Write your code here
        if not root:
            return 0
        cnt = 1
        cntLeft = self.helper(root.left, cnt, root.val)
        cntRight = self.helper(root.right, cnt, root.val)
        return max(cntLeft, cntRight)

    def helper(self, root, cnt, parentVal):
        if not root:
            return cnt
        if root.val == parentVal+1:
            cnt += 1
        else:
            cnt = 1
        leftVal = self.helper(root.left, cnt, root.val)
        rightVal = self.helper(root.right, cnt, root.val)
        return max(cnt, max(leftVal, rightVal))

        #traversal + divide conquer