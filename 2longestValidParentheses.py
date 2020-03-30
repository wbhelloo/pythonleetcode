from typing import List


class Solution:
    def isvalid(self, s: str) -> bool:
        length = len(s)
        left = 0
        for i in range(length):
            if s[i] == '(':
                left += 1
            else:
                left -=1
            if left < 0:
                return False
        if left == 0:
            return True
        else:
            return False

    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        length = len(s)
        res = 0
        for i in range(length):
            for j in range(i, length):
                tmp = s[i:j+1]
                if self.isvalid(tmp) and len(s[i:j+1]) > res:
                    res = len(s[i:j+1])
        return res


if __name__ == '__main__':
    sol = Solution()
    s = '()'
    print(sol.isvalid(s))
