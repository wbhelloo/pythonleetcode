from typing import List


class Unionfind:
    def __init__(self, n):
        self.nums = [i for i in range(n)]
        self.count = n
        self.depth = [1] * n

    def find(self, x):
        while self.nums[x] != x:
            self.nums[x] = self.nums[self.nums[x]]  # 压缩路径
            x = self.nums[x]
        return x

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.depth[rx] < self.depth[ry]:
                self.nums[rx] = ry
            elif self.depth[rx] > self.depth[ry]:
                self.nums[ry] = rx
            else:
                self.nums[ry] = rx
                self.depth[rx] += 1
            self.count -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = Unionfind(n)
        for i, j in edges:
            union_find.union(i, j)
        return union_find.count


if __name__ == '__main__':
    sol = Solution()
    print(sol.countComponents(n=6, edges=[[0, 1], [1, 2], [3, 4], [4, 5]]))
