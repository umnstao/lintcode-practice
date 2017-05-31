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
    @return: True if the binary tree is BST, or false
    """

        '''
    # Method 1: Traverse: Succinct
    isBst = True
    lastVal = None
    def isValidBST(self, root):
        self.inorderCheck(root)
        return self.isBst

    def inorderCheck(self, root):
        if not root:
            return
        self.inorderCheck(root.left)
        if self.lastVal is not None and root.val <= self.lastVal:
            self.isBst = False
        self.lastVal = root.val
        self.inorderCheck(root.right)

    # Method 2: Traverse: Obsolete
    def isValidBST(self, root):
        myL = []
        self.inorder(root, myL)
        for i in xrange(1,len(myL)):
            if myL[i] - myL[i-1] <= 0 :
                return False
        return True

    def inorder(self, root, myL):
        if root is None:
            return
        self.inorder(root.left, myL)
        myL.append(root.val)
        self.inorder(root.right, myL)

    # Method 3: Divide and conquer
    def isValidBST(self, root):
        return self.helper(root, -float('inf'), float('inf'))
    def helper(self, root, leftmax, rightmin):
        if root is None:
            return True
        if root.val > leftmax and root.val < rightmin:
            return self.helper(root.left, leftmax, root.val) \
            and self.helper(root.right, root.val, rightmin)
        else:
            return False
        '''