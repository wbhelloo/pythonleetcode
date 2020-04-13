from typing import List


class Solution:
    # 分奇偶
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0:
            return True

        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
            if i + 1 < n:
                dp[i][i + 1] = max(nums[i], nums[i + 1])

        # 转移方程dp[i][j] = max(nums[i] + min(dp[i-1][j-1],dp[i-2][j]),
        # nums[j] + min(dp[i-1][j-1],dp[i][j-2])

        for i in range(n-1, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = max(nums[i] + min(dp[i + 1][j - 1], dp[i + 2][j]),
                               nums[j] + min(dp[i + 1][j - 1], dp[i][j - 2]))
        return dp[0][n - 1] >= sum(nums) / 2


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(sol.PredictTheWinner(nums))
