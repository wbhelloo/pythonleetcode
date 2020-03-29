class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not s:
            return True

        for i in range(len(s)):
            if s[i] in ('[', '{', '('):
                stack.append(s[i])
            else:
                if s[i] == ')' and stack and stack[-1] == '(':
                    stack.pop()
                    continue
                elif s[i] == ']' and stack and stack[-1] == '[':
                    stack.pop()
                    continue
                elif s[i] == '}' and stack and stack[-1] == '{':
                    stack.pop()
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False

if __name__ == '__main__':
    sol=Solution()
    s = "()[]{}"
    print(sol.isValid(s))
