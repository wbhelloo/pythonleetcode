class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        remain = len(num) - k
        stack = []
        for s in num:
            while stack and stack[-1] > s and k > 0:
                stack.pop()
                k -= 1
            stack.append(s)
        res = ''.join(stack[:remain]).lstrip('0')
        return '0' if res == '' else res


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeKdigits(num="1432219", k=3))
