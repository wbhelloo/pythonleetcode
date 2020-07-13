from collections import defaultdict


class Solution:
    def __init__(self):
        self.record = defaultdict(lambda: False)

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (s1, s2, s3) in self.record.keys():
            return self.record[(s1, s2, s3)]
        if len(s1) + len(s2) != len(s3):
            self.record[s1, s2, s3] = False
            return self.record[(s1, s2, s3)]
        if not s1:
            self.record[(s1, s2, s3)] = (s2 == s3)
            return self.record[(s1, s2, s3)]
        if not s2:
            self.record[(s1, s2, s3)] = (s1 == s3)
            return self.record[(s1, s2, s3)]
        if not s3:
            self.record[(s1, s2, s3)] = False
            return self.record[(s1, s2, s3)]
        index1 = s3.find(s1[0])
        index2 = s3.find(s2[0])
        if index1 == index2 != -1:
            self.record[s1, s2, s3] = self.isInterleave(s1[1:], s2, s3[index1 + 1:]) \
                                      or self.isInterleave(s1, s2[1:], s3[index2 + 1:])
        elif -1 != index1 < index2:
            self.record[s1, s2, s3] = self.isInterleave(s1[1:], s2, s3[index1 + 1:])
        elif -1 != index2 < index1:
            self.record[s1, s2, s3] = self.isInterleave(s1, s2[1:], s3[index2 + 1:])
        return self.record[s1, s2, s3]

    def isInterleaveDP(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        # 初始化dp 包括第一行和第一列
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):  # 初始化第一列
            dp[i][0] = dp[i - 1][0] and (s3[i - 1] == s1[i - 1])
        for i in range(1, n + 1):  # 初始化第一行
            dp[0][i] = dp[0][i - 1] and (s3[i - 1] == s2[i - 1])

        # 计算所有dp值
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 状态方程
                dp[i][j] = (dp[i - 1][j] and (s3[i + j - 1] == s1[i - 1])) or (
                            dp[i][j - 1] and (s3[i + j - 1] == s2[j - 1]))

        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
    print(sol.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
    print(sol.isInterleave(s1="", s2="", s3="a"))
