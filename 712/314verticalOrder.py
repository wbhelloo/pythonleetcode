from collections import defaultdict
from copy import deepcopy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def verticalOrder(self, root: TreeNode):
        """将左边标记为root.val-1，右边为root.val+1"""
        if not root:
            return []
        record = defaultdict(list)
        curr = [[root, 0]]
        while curr:
            nxt = []
            for node, val in curr:
                record[val].append(node)
                if node.left:
                    nxt.append([node.left, val - 1])
                if node.right:
                    nxt.append([node.right, val + 1])
            curr = nxt
        return [record[v] for v in sorted(record.keys())]


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    tt = sol.verticalOrder(root)
    print([n.val for t in tt for n in t])
