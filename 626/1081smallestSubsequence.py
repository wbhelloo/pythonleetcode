class Solution:
    def smallestSubsequence(self, text: str) -> str:
        count = dict()
        for s in text:
            count[s] = count.get(s, 0) + 1
        stack = []
        for s in text:
            if s in stack:
                count[s] -= 1
                continue
            while stack and stack[-1] > s and count[stack[-1]] > 1:
                tmp = stack.pop()
                count[tmp] -= 1
            stack.append(s)
        return ''.join(stack)


if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestSubsequence(text="bcbcbcababa"))
