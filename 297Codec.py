from typing import List
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
        res = ''

        def serializeHelp(r, string):
            if r is None:
                string += 'None,'
            else:
                string += str(r.val) + ','
                string = serializeHelp(r.left, string)
                string = serializeHelp(r.right, string)
            return string

        return serializeHelp(root, res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def deserializeHelp(l: List[str]):
            if not l:
                return
            if l[0] == 'None':
                l.pop(0)
                return None
            root1 = TreeNode(l[0])
            l.pop(0)
            root1.left = deserializeHelp(l)
            root1.right = deserializeHelp(l)
            return root1

        tree = data.split(',')
        return deserializeHelp(tree)


# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    codec = Codec()
    root = '1,2,3,None,None,4,None,None,5,None,None'
    print(codec.serialize(codec.deserialize(root)))
