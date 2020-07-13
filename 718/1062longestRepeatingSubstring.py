class Solution(object):
    def longestRepeatingSubstring(self, S: str) -> int:
        """
        dp[(i, j)]表示以i, j结尾的重复子串长度
        """
        dp = dict()
        n = len(S)
        for i in range(n):
            for j in range(i+1, n):
                if S[i] == S[j]:
                    dp[(i, j)] = dp.get((i-1, j-1), 0) + 1
        return max(dp.values()) if dp.values() else 0



if __name__ == '__main__':
    sol = Solution()
    print(sol.longestRepeatingSubstring(S="abcd"))
    print(sol.longestRepeatingSubstring(S="abbaba"))
    print(sol.longestRepeatingSubstring(S="aabcaabdaab"))
    print(sol.longestRepeatingSubstring(S="aaaaa"))
