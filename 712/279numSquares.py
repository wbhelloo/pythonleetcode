import math
"""https://zhuanlan.zhihu.com/p/141580934"""

class Solution:
    def numSquares(self, n):
        res = n

        def helper(curr, tmp):
            nonlocal res
            if curr == 0:
                res = min(res, tmp)
                return
            if curr < 0:
                return

            right = math.floor(math.sqrt(n))
            for j in range(right, max(right - 4, 0), -1):
                helper(curr - j * j, tmp + 1)

        helper(n, 0)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(n=12))
    print(sol.numSquares(n=16))
