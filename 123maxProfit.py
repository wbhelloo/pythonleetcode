from typing import List


# dp[3][2][1] 的含义就是：今天是第三天，我现在手上持有着股票，至今最多进行 2 次交易。
# 再比如 dp[2][3][0] 的含义：今天是第二天，我现在手上没有持有股票，至今最多进行 3 次交易。
#
# 我们想求的最终答案是 dp[n - 1][K][0]，即最后一天，最多允许 K 次交易，最多获得多少利润。
# 为什么不是 dp[n - 1][K][1]？因为 [1] 代表手上还持有股票，[0] 表示手上的股票已经卖出去了，很显然后者得到的利润一定大于前者。
#
# dp[-1][k][0] = 0
# 解释：因为 i 是从 0 开始的，所以 i = -1 意味着还没有开始，这时候的利润当然是 0 。
# dp[-1][k][1] = -infinity
# 解释：还没开始的时候，是不可能持有股票的，用负无穷表示这种不可能。
# dp[i][0][0] = 0
# 解释：因为 k 是从 1 开始的，所以 k = 0 意味着根本不允许交易，这时候利润当然是 0 。
# dp[i][0][1] = -infinity
# 解释：不允许交易的情况下，是不可能持有股票的，用负无穷表示这种不可能。
# 把上面的状态转移方程总结一下：
#
# base case：
# dp[-1][k][0] = dp[i][0][0] = 0
# dp[-1][k][1] = dp[i][0][1] = -infinity
#
# 状态转移方程：
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
# 这里k = 2
# dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
# dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])

# dp[-1][k][0] = dp[i][0][0] = 0
# dp[-1][k][1] = dp[i][0][1] = -infinity

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        num = len(prices)
        if num == 1:
            return 0

        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(num)]
        # dp[0][2][0] = max(dp[-1][2][0], dp[-1][2][1] + prices[i]) = 0
        # dp[0][2][1] = max(dp[-1][2][1], dp[-1][1][0] - prices[i]) = -prices[0]
        # dp[0][1][0] = max(dp[-1][0][0], dp[-1][0][1] + prices[i]) = 0
        # dp[0][1][1] = max(dp[-1][1][1], dp[-1][-1][0] - prices[i]) = -prices[0]
        dp[0][2][0] = 0
        dp[0][2][1] = -prices[0]
        dp[0][1][0] = 0
        dp[0][1][1] = -prices[0]

        for i in range(1, num):
            for k in range(2, 0, -1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return dp[num - 1][2][0]


if __name__ == '__main__':
    sol = Solution()
    nums = [6, 1, 3, 2, 4, 7]
    num2 = [1, 2, 3, 4, 5]
    print(sol.maxProfit(num2))
