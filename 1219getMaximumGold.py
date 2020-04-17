from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j, tmp):
            nonlocal col, row, curr, visit
            if tmp > curr:
                curr = tmp
            if i < 0 or i >= col or j < 0 or j >= row:
                return
            if visit[i][j] or grid[i][j] == 0:
                return
            visit[i][j] = True
            dfs(i - 1, j, tmp + grid[i][j])
            dfs(i + 1, j, tmp + grid[i][j])
            dfs(i, j - 1, tmp + grid[i][j])
            dfs(i, j + 1, tmp + grid[i][j])
            visit[i][j] = False

        res = 0
        if not grid:
            return 0
        col = len(grid)
        row = len(grid[0])
        for i in range(col):
            for j in range(row):
                curr = 0
                visit = [[False for _ in range(row)] for _ in range(col)]
                dfs(i, j, 0)
                if curr > res:
                    res = curr

        return res


if __name__ == '__main__':
    sol = Solution()
    grid = [[0,0,0,3,0,0,17,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,8,5,15,0,0],[0,0,0,0,0,17,0,17,0,0,12,0],[0,0,0,4,0,0,20,0,0,0,0,0],[0,0,0,0,0,7,13,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,16,20],[2,0,0,4,0,0,0,16,0,4,0,0],[0,0,11,0,0,10,0,0,5,0,0,18],[2,0,12,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,3,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
    print(sol.getMaximumGold(grid))
