from typing import List


class Solution:
    # 并查集
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find_root(r):
            nonlocal pre
            while pre[r] != r:
                r = pre[r]
            return r

        num = len(edges)
        pre = [i for i in range(num + 1)]  # 每个元素自成一个
        res = []
        for x, y in edges:
            tx, ty = find_root(x), find_root(y)
            if tx != ty:
                pre[ty] = tx
                continue
            res = [x, y]
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [[1, 2], [1, 3], [2, 3]]
    print(sol.findRedundantConnection(nums))
