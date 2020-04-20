from typing import List


# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        num = len(prices)
        if num == 1:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(num)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(0, dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], - prices[1])
        for i in range(2, num):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[num - 1][0]


if __name__ == '__main__':
    sol = Solution()
    nums = [6, 1, 3, 2, 4, 7]
    num2 = [1, 2, 3, 0, 2]
    print(sol.maxProfit(num2))
