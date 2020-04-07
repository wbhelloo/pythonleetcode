# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten1(self, root: TreeNode):
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            pre = root.left
            while pre.right:
                pre = pre.right
            pre.right = root.right
            root.right = root.left
            root.left = None

    def flatten(self, root: TreeNode):
        pre = None

        def flattenPe(root1):
            if root1 is None:
                return
            flattenPe(root1.right)
            flattenPe(root1.left)
            nonlocal pre
            root1.right = pre
            root1.left = None
            pre = root1

        flattenPe(root)
