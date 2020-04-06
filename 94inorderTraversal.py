from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversalBack(self, root: TreeNode) -> List[int]:
        res = []
        self.inorderTraversalGre(root, res)
        return res

    def inorderTraversalGre(self, root: TreeNode, res):
        if root == None:
            return
        if root.left != None:
            self.inorderTraversalGre(root.left, res)
        res.append(root.val)
        if root.right != None:
            self.inorderTraversalGre(root.right, res)

    def inorderTraversal(self, root: TreeNode) -> List[int]:

        stack = []
        p = root
        res = []
        while stack or p is not None:
            if p is not None:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                res.append(p.val)
                p = p.right
        return res
