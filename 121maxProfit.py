from typing import List


# base case：
# dp[-1][k][0] = dp[i][0][0] = 0
# dp[-1][k][1] = dp[i][0][1] = -infinity
#
# 状态转移方程：
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
# 本题目k=1
# 也就是
# dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
# dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][-1][0] - prices[i])
# 这里dp[i-1][-1][0] = 0
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], - prices[i])

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        num = len(prices)
        if num == 1:
            return 0
        dp = [0 for _ in range(num)]
        for i in range(1, num):
            dp[i] = max(dp[i], prices[i] - prices[i - 1] + dp[i - 1])

        return max(dp)

    def maxProfitTL(self, prices: List[int]) -> int:
        if not prices:
            return 0
        num = len(prices)
        if num == 1:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(num)]
        # dp[0][0] = max(dp[-1][0], dp[-1][1] + prices[i]) = 0
        dp[0][0] = 0
        # dp[0][1] = max(dp[-1][1],- prices[0])
        dp[0][1] = -prices[0]
        for i in range(1, num):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], - prices[i])

        return dp[num - 1][0]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2]
    print(sol.maxProfitTL(nums))
