from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0

        def dfs(start, tmp):
            nonlocal arr, res
            if len(tmp) > res:
                res = len(tmp)
            if start >= len(arr):
                return
            if len(set(list(arr[start]) + tmp)) == len(tmp) + len(list(arr[start])):
                dfs(start + 1, list(arr[start]) + tmp)
            dfs(start + 1, tmp)

        dfs(0, [])
        return res


if __name__ == '__main__':
    sol = Solution()
    arr = ["cha", "r", "act", "ers"]
    print(sol.maxLength(arr))
