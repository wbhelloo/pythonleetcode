class Solution:
    def numTrees(self, n: int) -> int:

        dp = [0 for _ in range(n + 1)]

        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


if __name__ == '__main__':
    sol=Solution()
    n=3
    print(sol.numTrees(n))
