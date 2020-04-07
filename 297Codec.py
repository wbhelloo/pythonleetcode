# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return

        pre = [root]
        net = []
        res = []
        while pre:
            for p in pre:
                if p is None:
                    res.append(None)
                    net.append(None)
                    continue
                res.append(p.val)
                if p.left is None:
                    net.append(None)
                else:
                    net.append(p.left)
                if p.right is None:
                    net.append(None)
                else:
                    net.append(p.right)
            pre = net
            net = []
        return res




    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
