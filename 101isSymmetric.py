# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSymmetricTwo(root, root)

    def isSymmetricTwo(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None:
            return root2 is None
        left = False
        right = False
        if root1 is not None and root2 is not None:
            left = self.isSymmetricTwo(root1.left, root2.right) and root1.val == root2.val
            right = self.isSymmetricTwo(root1.right, root2.left) and root1.val == root2.val
        return left and right
