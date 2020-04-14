class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        snum = len(s)
        tnum = len(t)

        i, j = 0, 0
        while i < snum and j < tnum:
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == snum:
            return True
        return False


if __name__ == '__main__':
    sol = Solution()
    s = "axc"
    t = "bbaxc"
    print(sol.isSubsequence(s, t))
