# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isValidBSTSolve(root)

    def isValidBSTSolve(self, root: TreeNode, lower=float('-inf'), upper=float('inf')) -> bool:

        left = True
        right = True
        if lower < root.val < upper:
            if root.left is not None:
                left = self.isValidBSTSolve(root.left, lower=lower, upper=root.val)
            if root.right is not None:
                right = self.isValidBSTSolve(root.right, lower=root.val, upper=upper)
            return left and right
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(10, (5, None, None), (15, 6, 20))
    print(sol.isValidBST(tree))
