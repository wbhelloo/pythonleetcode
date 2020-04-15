# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []

        def helper(root):
            nonlocal k,res
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        if k > len(res):
            return 0
        return res[k-1]


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)
    root.right.right = TreeNode(5)
    print(sol.kthSmallest(root, 3))
