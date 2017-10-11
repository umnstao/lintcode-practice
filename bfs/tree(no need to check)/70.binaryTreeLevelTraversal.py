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
    @return: buttom-up level order in a list of lists of integers
    """
    def levelOrderBottom(self, root):
        # write your code here
        result = []
        if not root:
            return result
        q = [root]

        while q:
            size = len(q)
            level = []
            for _ in range(size):
                head = q.pop(0)
                level.append(head.val)
                if head.left:
                    q.append(head.left)
                if head.right:
                    q.append(head.right)
            result.insert(0,level)

        return result
