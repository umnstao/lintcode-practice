"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        ret = []
        if not root:
            return ret
        q = [root]

        while len(q) > 0:
            size = len(q)
            dummy = ListNode(-1)
            curr = dummy
            for _ in xrange(size):
                treeNode = q.pop(0)
                tmpNode = ListNode(treeNode.val)
                curr.next = tmpNode
                curr = tmpNode
                if treeNode.left:
                    q.append(treeNode.left)
                if treeNode.right:
                    q.append(treeNode.right)
            ret.append(dummy.next)
        return ret
