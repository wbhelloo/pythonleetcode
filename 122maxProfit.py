from typing import List

# base case：
# dp[-1][k][0] = dp[i][0][0] = 0
# dp[-1][k][1] = dp[i][0][1] = -infinity
#
# 状态转移方程：
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
# 本题目k为无穷
# 也就是
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
# 这里
# dp[0][0] = 0
# dp[0][1] = - prices[0]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        num = len(prices)
        if num == 1:
            return 0

        res = 0
        for i in range(1,num):
            tmp = prices[i]- prices[i-1]
            res+=(tmp if tmp > 0 else 0)
        return res

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
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[num - 1][0]

if __name__ == '__main__':
    sol = Solution()
    nums = [7,1,5,3,6,4]
    print(sol.maxProfit(nums))
