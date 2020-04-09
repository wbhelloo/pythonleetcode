from typing import List


class Solution:
    def reverseWordsBL(self, s: str) -> str:
        rever = s[::-1]
        split = rever.strip().split(' ')
        res = ''
        for sp in split:
            if sp == '':
                continue
            res += sp[::-1].strip()+' '
        return res.strip()

    def reverseWords(self, s: str) -> str:
        #return " ".join(reversed(s.split()))
        word = [sp.strip()[::-1] for sp in s[::-1].strip().split()]
        return ' '.join(word)


if __name__ == '__main__':
    sol = Solution()
    s1 = "  hello world!  "
    s = "a good   example"
    print(sol.reverseWords(s))
