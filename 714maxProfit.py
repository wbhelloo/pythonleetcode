from typing import List

class Solution(object):
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
    # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
    # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    # 这里
    # dp[0][0] = 0
    # dp[0][1] = - prices[0]
    def maxProfitTL(self, prices, fee):
        if not prices:
            return 0
        num = len(prices)
        if num == 1:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(num)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, num):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[num-1][0]



if __name__ == '__main__':
    sol = Solution()
    prices = [2,2,1,1,5,5,3,1,5,4]
    fee = 2
    print(sol.maxProfit(prices, fee))
