from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        if not S:
            return []

        res = []

        def dfs(sub: str, first: int, second: int, tmp: List[int]):
            nonlocal res

            if tmp[-1] > 2 ** 31 - 1:
                return False

            if not sub:
                res = tmp
                return True

            curr = first + second
            currstr = str(curr)

            if sub.startswith(currstr):
                return dfs(sub[len(currstr):], second, curr, tmp + [first + second])
            else:
                return False

        num = len(S)
        for i in range(1, num // 2 + 1):
            for j in range(i + 1, num):
                if (S[i] == '0' and j > i + 1) or (S[0] == '0' and i > 1):
                    continue
                one = int(S[:i])
                two = int(S[i:j])
                if dfs(S[j:], one, two, [one, two]):
                    return res
        else:
            return []


if __name__ == '__main__':
    sol = Solution()
    s = "2820022842865610841740282445647388119521934031292"
    print(sol.splitIntoFibonacci(s))
