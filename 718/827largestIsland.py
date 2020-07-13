from typing import List
from copy import deepcopy


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        def bfs(row, col, num):
            """编号人工岛为num"""
            curr = [[row, col]]
            grid[row][col] = num

            res = 1
            while curr:
                nxt = []
                for i, j in curr:
                    for x, y in dir:
                        if 0 <= i + x < rows and 0 <= j + y < cols and grid[i + x][j + y] == 1:
                            nxt.append([i + x, j + y])
                            res += 1
                            grid[i + x][j + y] = num
                curr = deepcopy(nxt)
            return res

        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        all_sum = sum(grid[i][j] for i in range(rows) for j in range(cols))
        if all_sum == 0:
            return 1
        if all_sum == cols * rows:
            return all_sum

        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        flag = 2
        record = dict()
        sea = set()
        for i in range(rows):
            for j in range(cols):
                # 不同人工岛编号
                if grid[i][j] == 1:
                    record[flag] = bfs(i, j, flag)
                    flag += 1
                if grid[i][j] == 0:
                    sea.add((i, j))

        res = 0
        for i, j in sea:
            tmp = 0
            if grid[i][j] == 0:
                cur = set()
                for x, y in dir:
                    if 0 <= i + x < rows and 0 <= j + y < cols \
                            and grid[i + x][j + y] != 0 and grid[i + x][j + y] not in cur:
                        tmp += record[grid[i + x][j + y]]
                        cur.add(grid[i + x][j + y])
            res = max(tmp, res)
        return res + 1

    def largestIslandBL(self, grid: List[List[int]]) -> int:
        """找人工岛的位置60/63"""

        def bfs(row, col):
            visit = [[False for _ in range(cols)] for _ in range(cols)]
            res = 1
            curr = [[row, col]]

            while curr:
                nxt = []
                for i, j in curr:
                    for x, y in dir:
                        if 0 <= i + x < rows and 0 <= j + y < cols and grid[i + x][j + y] and not \
                                visit[i + x][j + y]:
                            nxt.append([i + x, j + y])
                            visit[i + x][j + y] = True
                            res += 1
                curr = deepcopy(nxt)
            return res

        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        all_sum = sum(grid[i][j] for i in range(rows) for j in range(cols))
        if all_sum == 0:
            return 1
        if all_sum == cols * rows:
            return all_sum

        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        for i in range(rows):
            for j in range(cols):
                # 该点可作为连接点
                if grid[i][j] == 0 and sum(
                        grid[i + x][j + y] for x, y in dir if 0 <= i + x < rows and 0 <= j + y < cols):
                    res = max(res, bfs(i, j))
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestIsland(grid=[[1, 1], [1, 0]]))
