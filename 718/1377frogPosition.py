from typing import List
from collections import defaultdict


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if not edges:
            return 1 if n == 1 else 0
        front = defaultdict(list)
        rever = defaultdict(list)
        for u, v in edges:
            front[u].append(v)
            rever[v].append(u)
        if 1 in rever.keys():
            front, rever = rever, front

        res = 1
        count = 0
        if target not in rever.keys():
            return 0
        up = target
        while up in rever.keys() and up != 1:
            up, *other = rever[up]
            res = res * 1 / len(front[up])
            count += 1
        if front[target] and count == t:
            return res
        if not front[target] and count <= t:
            return res
        return 0


if __name__ == '__main__':
    sol = Solution()
    # print(sol.frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=2, target=4))
    # print(sol.frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=1, target=7))
    print(sol.frogPosition(n=8, edges=[[2, 1], [3, 2], [4, 1], [5, 1], [6, 4], [7, 1], [8, 7]], t=7, target=7))
    print(sol.frogPosition(n=1, edges=[], t=1, target=1))
