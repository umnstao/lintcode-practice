"""
This includes all important codes about tree

-binary tree
-binary search tree
-all general tree

Definition:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

"""

# traverse
class traverse:
    def preorder(self, root):
        if not root:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)
    def inorder(self, root):
        if not root :
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    def postorder(self, root):
        if not root:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.val]

    def preorder_iterative(self, root):
        stack = [root]
        preorder = []
        while len(stack) > 0:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder

    def inorder_iterative(self, root):
        inorder = []
        stack = []
        node = root
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            inorder.append(node.val)
            node = node.right
        return inorder

# BST
class validBST:
    isBst = True
    lastVal = None

    def validate(self, root):
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








