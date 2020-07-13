"""
# Definition for a Node.
"""
from copy import deepcopy


class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """有问题"""
        def dfs(source, target):
            target.val = source.val
            visit.append(target)

            for neigh in source.neighbors:
                for v in visit:
                    if v.val == neigh.val:
                        target.neighbors.append(v)
                    break
                else:
                    tmp = Node()
                    dfs(neigh, tmp)
                    target.neighbors.append(deepcopy(tmp))

        root = Node()
        visit = []
        dfs(node, root)
        return root

    def cloneGraphgood(self, node: 'Node') -> 'Node':
        def dfs(source):
            if not source:
                return
            if source in visit.keys():
                return visit[source]
            clone = Node(source.val, [])
            visit[source] = clone
            for neigh in source.neighbors:
                clone.neighbors.append(dfs(neigh))

            return visit[source]

        visit = dict()
        return dfs(node)
