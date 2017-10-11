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
    @return: A list of list of integer include
             the zig zag level order traversal of its nodes' values
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        result = []
        if not root:
            return result
        q  = [root]
        reverseOrder = False
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                head = q.pop(0)
                if not reverseOrder:
                    level.append(head.val)
                else:
                    level.insert(0,head.val)
                if head.left:
                    q.append(head.left)
                if head.right:
                    q.append(head.right)
            result.append(level)
            reverseOrder = not reverseOrder
        return result

def zigzagLevelOrder(self, root):
        # write your code here
        result = []
        if not root:
            return result
        q  = [root]
        reverseOrder = False
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                head = q.pop(0)
                if not reverseOrder:
                    level.append(head.val)
                else:
                    level.insert(0,head.val)
                if head.left:
                    q.append(head.left)
                if head.right:
                    q.append(head.right)
            result.append(level)
            reverseOrder = not reverseOrder
        return result
