# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    # Method 1: Any binary tree + O(n) space
    def inorderSuccessor(self, root, p):
        # write your code here
        myList = self.inorder(root)
        for i in xrange(len(myList)):
            if myList[i] == p:
                if i is not len(myList)-1:
                    return myList[i+1]
        return None

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root] + self.inorder(root.right)

    # Method 2: Any binary tree + O(1) space
    lastNode = None
    ret = None
    def inorderSuccessor(self, root, p):
        # write your code here
        self.inorder(root, p)
        return self.ret

    def inorder(self, root, p):
        if not root:
            return None
        self.inorder(root.left, p)
        if self.lastNode is not None and self.lastNode == p:
            self.ret = root
        self.lastNode = root
        self.inorder(root.right, p)

    # Method 3: BST + O(1) space