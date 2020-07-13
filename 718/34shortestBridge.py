from typing import List
from copy import deepcopy


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:

        def dfs(row, col):
            nonlocal record
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if A[row][col] != 1:
                return
            A[row][col] = 2
            record.append((row, col))
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        rows = len(A)
        cols = len(A[0])
        bridge = []
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1:
                    record = []
                    dfs(i, j)
                    bridge.append(deepcopy(record))
        curr = set(bridge[0])
        target = set(bridge[1])
        res = 0
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while curr:
            nxt = set()
            for i, j in curr:
                for x, y in dir:
                    if 0 <= i + x < rows and 0 <= j + y < cols:
                        nxt.add((i + x, j + y))

            if nxt & target:
                break
            res += 1
            curr = deepcopy(nxt)
        return res


if __name__ == '__main__':
    sol = Solution()
    # print(sol.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))
    print(sol.shortestBridge([[0, 1, 0, 0, 0], [0, 1, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
