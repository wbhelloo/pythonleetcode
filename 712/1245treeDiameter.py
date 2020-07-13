from typing import List
from collections import defaultdict


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        num = len(edges) + 1
        visit = [False for _ in range(num)]
        record = defaultdict(list)
        for u, v in edges:
            record[u].append(v)
            record[v].append(u)
        res = 0

        def helper(start, curr):
            nonlocal res, visit
            if curr > res:
                res = curr
            if visit[start]:
                return
            visit[start] = True
            for nxt in record[start]:
                helper(nxt, curr + 1)

        for i in range(num):
            helper(i, 0)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.treeDiameter(edges=[[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]))
    print(sol.treeDiameter(edges=[[0, 1], [0, 2]]))
