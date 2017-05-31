"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
class Solution:
    """
    @param root: The root of the tree
    @param A and B: Two node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # Write your code here
        pathA = self.generatePath([],A)
        pathB = self.generatePath([],B)
        idxA = len(pathA) - 1
        idxB = len(pathB) - 1
        while idxA >= 0 or idxB >= 0:
            if pathA[idxA] != pathB[idxB]:
                break
            lca = pathA[idxA]
            idxA -= 1
            idxB -= 1
        return lca

    def generatePath(self, path, node):
        while node:
            path.append(node)
            node = node.parent
        return path